#!/usr/bin/env python
#FIX: Rename this script Virtualize merra data?
# I would honestly love to make this a package (?) I could import elsewhere, that would be kind of cool

# Script used to process MERRA-2 data for fluxnet analysis

import xarray as xr
import sys
from MERRA2_query import find_MERRA2_files
from virtualizarr import open_virtual_dataset

#TODO: Turn these into path objects? Vzarr seems to use them?
# Symlink to MERRA-2 data
dir = '/discover/nobackup/hzafar/MERRA2_processing/MERRA2_all'

#NOTE: How am I going to select years, if Amerflux years varies across sites?
# AmeriFlux FLUXNET spans 1991-2021 across all the sites, individual sites vary, let's just start with that
start_yr, end_yr = [1991, 2021]
freq1 = "tavg"
freq2 = "M"
group = "slv"
varslist = ["T2M", "T10M" ,"PRECTOT"] # vars should work as a list now
vars = varslist[0]

fileslist = find_MERRA2_files(dir, freq1, freq2, group, str(start_yr), str(end_yr))
# print(type(fileslist))
# print(fileslist[-1])
ds_MERRA2 = xr.open_mfdataset(fileslist[:10])[vars]
# print(ds_MERRA2)

#TODO: Run this test?
virtual_datasets = [open_virtual_dataset(filepath, 
                                         loadable_variables=["time"],
                                         decode_times=True,
                                         ) for filepath in fileslist]

virtual_ds_combine = xr.concat(virtual_datasets, dim='time', coords='minimal',compat='override')
#FIX: try parquet? instead of json
virtual_ds_combine.virtualize.to_kerchunk('combined_test_loadable.json', format='json')

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
