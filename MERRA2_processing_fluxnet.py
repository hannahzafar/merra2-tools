#!/usr/bin/env python
# Script used to process MERRA-2 data for fluxnet analysis

import xarray as xr
import sys
from MERRA2_query import find_MERRA2_files

# Symlink to MERRA-2 data
dir = '/discover/nobackup/hzafar/MERRA2_processing/MERRA2_all'

#NOTE: How am I going to select years, if Amerflux years varies across sites?
# AmeriFlux FLUXNET spans 1991-2021 across all the sites, individual sites vary, let's just start with that
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
'''
