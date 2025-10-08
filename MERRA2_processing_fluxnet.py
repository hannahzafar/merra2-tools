#!/usr/bin/env python
# Script used to process MERRA-2 data for fluxnet analysis

import xarray as xr
import argparse
import sys


ds_MERRA2 = xr.open_mfdataset(flist)[var]

# Sel only N+S America
americas_MERRA2 = ds_MERRA2.sel(
    lon=slice(-170, -30),
    lat=slice(-60,80)
)

print(americas_MERRA2)
#FIX: doing the sel takes so long, I think I'm just gonna virtualize
#FIX: Make this script the generation of the virtualizarr
# create subfolders in this repo? One with my old code and one with this? Or fork my repo?



