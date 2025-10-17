#!/usr/bin/env python
# Test the virtual store created via create_vzarr_store

import xarray as xr

# Suppress fill values warning
import warnings
warnings.filterwarnings("ignore", category=xr.SerializationWarning)

# ds_test = xr.open_dataset('virtual_store/vstore.json', engine='zarr')
# print(ds_test)
# ds = xr.open_dataset("reference::virtual_store/vstore.json", engine="zarr", consolidated=False)

# Pass consolidated = False to suppress warning about .zmetadata
ds = xr.open_dataset("reference::virtual_store/vstore.parquet", engine="zarr", consolidated=False)
print(ds['T2M'])
#NOTE: This seems to work and doesn't require loading time variables???
