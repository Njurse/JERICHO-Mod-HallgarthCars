#!/usr/bin/env python3
"""Remux every .wav in this folder to 16-bit PCM with headroom.
Originals are moved into ./original/ before being overwritten."""
from pathlib import Path
import shutil
import wave

TARGET_SAMPWIDTH = 2      # 2 bytes = 16-bit (most compatible)
TARGET_RATE      = 0      # 0 = keep original rate; e.g. 44100 to force
PEAK_TARGET      = 0.90   # scale peaks to 90% full-scale (~-1 dBFS)
BACKUP_DIR       = "original"

try:
    import audioop                    # stdlib through Python 3.12
except ImportError:                   # Python 3.13+
    audioop = None
    import numpy as np


def convert(frames, sampwidth, nchannels, framerate):
    """Return (frames, sampwidth, framerate) converted/normalized."""
    if audioop is not None:
        if sampwidth != TARGET_SAMPWIDTH:
            frames = audioop.lin2lin(frames, sampwidth, TARGET_SAMPWIDTH)
            sampwidth = TARGET_SAMPWIDTH

        peak = audioop.max(frames, sampwidth)
        full = (1 << (sampwidth * 8 - 1)) - 1
        target = int(full * PEAK_TARGET)
        if peak > target > 0:
            frames = audioop.mul(frames, sampwidth, target / peak)

        rate = TARGET_RATE or framerate
        if rate != framerate:
            frames, _ = audioop.ratecv(
                frames, sampwidth, nchannels, framerate, rate, None)
            framerate = rate
        return frames, sampwidth, framerate

    # numpy fallback
    if sampwidth == 1:
        x = (np.frombuffer(frames, dtype=np.uint8).astype(np.float32) - 128) / 128
    elif sampwidth == 2:
        x = np.frombuffer(frames, dtype='<i2').astype(np.float32) / 32768
    elif sampwidth == 3:
        b = np.frombuffer(frames, dtype=np.uint8).reshape(-1, 3).astype(np.int32)
        v = b[:, 0] | (b[:, 1] << 8) | (b[:, 2] << 16)
        v = np.where(v >= 1 << 23, v - (1 << 24), v)
        x = v.astype(np.float32) / (1 << 23)
    elif sampwidth == 4:
        x = np.frombuffer(frames, dtype='<i4').astype(np.float32) / (1 << 31)
    else:
        raise ValueError(f"unsupported sample width: {sampwidth}")

    peak = float(np.max(np.abs(x))) if x.size else 0.0
    if peak > PEAK_TARGET:
        x = x * (PEAK_TARGET / peak)

    rate = TARGET_RATE or framerate
    if rate != framerate:
        n = int(round(len(x) * rate / framerate))
        x = np.interp(np.linspace(0, len(x) - 1, n),
                      np.arange(len(x)), x).astype(np.float32)
        framerate = rate

    y = np.clip(x * 32767, -32768, 32767).astype('<i2')
    return y.tobytes(), 2, framerate


def main():
    root = Path(__file__).resolve().parent
    backup = root / BACKUP_DIR
    backup.mkdir(exist_ok=True)

    wavs = [p for p in root.iterdir()
            if p.is_file() and p.suffix.lower() == ".wav"]
    if not wavs:
        print("no .wav files found next to this script")
        return

    for wav in sorted(wavs):
        tmp = wav.parent / (wav.name + ".tmp")
        try:
            with wave.open(str(wav), "rb") as w:
                params = w.getparams()
                frames = w.readframes(params.nframes)

            new_frames, sw, rate = convert(
                frames, params.sampwidth, params.nchannels, params.framerate)

            with wave.open(str(tmp), "wb") as w:
                w.setnchannels(params.nchannels)
                w.setsampwidth(sw)
                w.setframerate(rate)
                w.writeframes(new_frames)

            # pick a non-clobbering name in the backup folder
            dest = backup / wav.name
            i = 1
            while dest.exists():
                dest = backup / f"{wav.stem}.{i}{wav.suffix}"
                i += 1

            shutil.move(str(wav), str(dest))
            tmp.replace(wav)

            print(f"OK   {wav.name}  ->  {sw*8}-bit {rate} Hz  "
                  f"(backup: {BACKUP_DIR}/{dest.name})")
        except Exception as e:
            print(f"FAIL {wav.name}: {e}")
            if tmp.exists():
                tmp.unlink()


if __name__ == "__main__":
    main()