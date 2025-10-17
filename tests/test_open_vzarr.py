#!/usr/bin/env python
# Test the virtual store created via create_vzarr_store

import xarray as xr

# Suppress fill values warning
import warnings
warnings.filterwarnings("ignore", category=xr.SerializationWarning)

# Pass consolidated = False to suppress warning about .zmetadata
ds = xr.open_dataset("reference::virtual_store/vstore.parquet", engine="zarr", consolidated=False)
print(ds)
