HALLCHCG - one-car Driver 2 car-data bank
================================

Source: CHICAGO model 1
Destination model slot: 1

This bank carries ONE car: clean, damaged and low. Every other model
slot is -1.

Files:
  bank.json          the declaration (donor, slot order, cars)
  HALLCHCG.LEV / .LCF      installed copies of build/ (loadable pair)
  cars/              the car's editable OBJ/MTL, page PNGs and sounds
  donor/             the donor manifest and untouched lumps
  build/             the bake output: NAME.LEV/.LCF, NAME.json,
                     NAME.report.json, pages/, models/

Install:
  1. Put this folder where cities.ini can reach it.
  2. Add the line from cities.ini under [cities] in
     JERICHO/CONFIG/cities.ini.
  3. Import it with import = <resident slot>:<city index>:<model>.
     city_N has city index 11 (11 + N).

Stage scripts (written beside this file):
  wizard.bat    hub for every stage below
  rebake.bat    bake + install + register, then preview / ride
  preview.bat   pick a slot, endless preview until you quit
  playtest.bat  Take a Ride with a car, no bake

Rebuild after editing the car's OBJ or bank.json:
  rebake.bat
