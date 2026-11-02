# JERICHO-Mod-HallgarthCars
The showcase for BAKE - Hallgarth's Pontiac Firebird, lovingly crafted and imported for use in Driver 2 under the JERICHO carhacks ecosystem.

## Install
From the in-game mod store (Hallgarth's Cars), or copy this repo to `JERICHO/MODS/hallgarthcars/`.
Then add the `city_0` line from `banks/hallchcg/cities.ini` under `[cities]` in `JERICHO/CONFIG/cities.ini`
and import the car in `carhacks.ini` (`import = <slot>:<city index>:1`). See `banks/hallchcg/README.txt`.

## Rebuild
`banks/hallchcg/rebake.bat` (needs the BAKE tools; donor/ and build/ are generated locally and not shipped). The Firebird OBJs are already in engine units, so the bake runs with `--scale 1`.
