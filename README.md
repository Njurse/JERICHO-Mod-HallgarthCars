# JERICHO-Mod-HallgarthCars
The showcase for BAKE - Hallgarth's Pontiac Firebird, lovingly crafted and imported for use in Driver 2 under the JERICHO carhacks ecosystem.

## Install
From the in-game mod store (Hallgarth's Cars): install, enable, play. carhacks (JERICHO 0.13.4+) registers the
HALLCHCG bank on its own, and the Firebird shows up in the car menu under HALLCHCG.

Older games, or a hand copy to `JERICHO/MODS/hallgarthcars/`: add the `city_1` line from
`banks/hallchcg/cities.ini` under `[cities]` in `JERICHO/CONFIG/cities.ini`. See `banks/hallchcg/README.txt`.

## What's new in 0.1.3
- The Firebird was re-exported and rebaked: updated clean, damaged and low geometry, paint pages 65/66/67 with a body-colour palette, and refreshed handling.
- The bank keeps the HALLCHCG name, so installing 0.1.3 over 0.1.2 replaces the car instead of adding a second one.

## Rebuild
`banks/hallchcg/rebake.bat` (needs the BAKE tools; donor/ and build/ are generated locally and not shipped). The Firebird OBJs are already in engine units, so the bake runs with `--scale 1`.
