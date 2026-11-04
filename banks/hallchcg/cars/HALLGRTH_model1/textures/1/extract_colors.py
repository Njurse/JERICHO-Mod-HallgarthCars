import sys
from PIL import Image
from collections import Counter

def top_colors(path, n=6):
    img = Image.open(path).convert("RGB")
    pixels = [p for p in img.getdata() if 30 < sum(p) < 700]
    snapped = [((r >> 3) << 3, (g >> 3) << 3, (b >> 3) << 3) for r, g, b in pixels]
    common = Counter(snapped).most_common(n)
    return [f"{r:02x}{g:02x}{b:02x}" for (r, g, b), _ in common]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Drop image files onto this script, or pass paths as arguments.")
        sys.exit(1)

    for path in sys.argv[1:]:
        try:
            colors = top_colors(path)
            print(f"{path}:")
            print("  " + ", ".join(colors))
            print()
        except Exception as e:
            print(f"{path}: error — {e}\n")
