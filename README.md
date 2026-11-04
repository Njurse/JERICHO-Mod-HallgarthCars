# JERICHO-Mod-HallgarthCars
The showcase for BAKE - Hallgarth's Pontiac Firebird, lovingly crafted and imported for use in Driver 2 under the JERICHO carhacks ecosystem.

## Install
From the in-game mod store (Hallgarth's Cars): install, then **Mods → enable** Hallgarth's Cars, then play.
`default-enabled` is false, so packbanks (carhacks 0.2.7+) registers HALLCHCG only after that enable
writes `hallgarthcars = 1` in `modlist.ini`. The Firebird shows up in the car menu under HALLCHCG.

Older games, or a hand copy to `JERICHO/MODS/hallgarthcars/`: add the `city_1` line from
`banks/hallchcg/cities.ini` under `[cities]` in `JERICHO/CONFIG/cities.ini`. See `banks/hallchcg/README.txt`.

## What's new in 0.1.4
- Placeholder / load fix. Clean, damaged and low now use texture sets that `handling.json` declares and that the tree ships: pages 65, 66 and 67, plus wheel set 50 (`banks/hallchcg/shared/textures/PAGE_50.png`).
- Damaged temporarily uses the clean mesh `Firebird_high.obj` (`PAGE_65`, `PAGE_66`, `PAGE_67` in `Firebird_high.mtl`). No damaged Firebird mesh on those pages is in the tree. `CHICAGO_model1_damaged.obj` still names `set1_id0_ft`, and `CHICAGO_model1.mtl` maps that at `textures/PAGE_1.png`, which `textures{}` does not declare and which is not under `cars/HALLGRTH_model1/textures/`. A missing set skips those polys and the host can fall back to the placeholder car. A wrecked Firebird keeps the clean body until a damaged mesh on pages 65/66/67 exists.
- Low stays `Firebird_low_scaled.obj` (`set65_id12` and `flat` in `Firebird_low.mtl`, both `textures/PAGE_65.png`). Wheels stay on set 50.

**NOTE — rebake on Babou before the store zip.** This checkout has no `bake/tools/car/carbank_bake.py` and no `banks/hallchcg/donor/`. `banks/hallchcg/HALLCHCG.LEV` (186368 bytes) and `HALLCHCG.LCF` are still the 0.1.3 bake. They still carry the old damaged model. Publish `hallgarthcars-0.1.4.zip` only after Babou runs `banks/hallchcg/rebake.bat` (it calls `bake\tools\car\carbank_bake.py` on `bank.json` with `--scale 1` and copies `build/HALLCHCG.LEV` and `build/HALLCHCG.LCF` onto this folder) and those two files are the new bake. Keep the bank city name `HALLCHCG`.

## What's new in 0.1.3
- The Firebird was re-exported and rebaked: updated clean, damaged and low geometry, paint pages 65/66/67 with a body-colour palette, and refreshed handling.
- The bank keeps the HALLCHCG name, so installing 0.1.3 over 0.1.2 replaces the car instead of adding a second one.

## Rebuild
`banks/hallchcg/rebake.bat` (needs the BAKE tools; donor/ and build/ are generated locally and not shipped). The Firebird OBJs are already in engine units, so the bake runs with `--scale 1`.
