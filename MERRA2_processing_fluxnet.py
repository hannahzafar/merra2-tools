#!/usr/bin/env python
# Script used to process MERRA-2 data for fluxnet analysis

import xarray as xr
import sys
from MERRA2_query import find_MERRA2_files

dir = '/discover/nobackup/hzafar/MERRA2_processing/MERRA2_all' # Made a new symlink to MERRA-2 data

#NOTE: How am I going to select years? If Amerflux varies? Similar to MiCASA I suppose, or should I look at all the years I have a record from and average across long time series??? 
# AmeriFlux FLUXNET spans 1991-2021 across all the sites, individual sites vary, let's just start with thisk
start_yr, end_yr = [1991, 2021]
freq1 = "tavg"
freq2 = "M"
group = "slv"
vars = ["T2M"]
# varlist = ["T2M", "T10M" ,"PRECTOT"]

fileslist = find_MERRA2_files(dir, freq1, freq2, group, str(start_yr), str(end_yr))
# print(type(fileslist))
# print(fileslist[-1])
ds_MERRA2 = xr.open_dataset(fileslist[0])[vars]
# print(ds_MERRA2)

'''
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
'''
