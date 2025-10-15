""" Insert description """
import xarray as xr
import sys
from virtualizarr import open_virtual_dataset

from .config import MERRA2_ROOT
from .query import find_MERRA2_files

ds_MERRA2 = xr.open_mfdataset(fileslist[:10])[vars]
# print(ds_MERRA2)

def create_vzarr_store(filepaths):
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
