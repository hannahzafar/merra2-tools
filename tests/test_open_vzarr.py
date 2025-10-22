#!/usr/bin/env python
# Test the virtual store created via create_vzarr_store

import xarray as xr
import matplotlib.pyplot as plt

# Suppress fill values warning
import warnings

warnings.filterwarnings("ignore", category=xr.SerializationWarning)

# Pass consolidated = False to suppress warning about .zmetadata
# Test a few years (same compression type)
# ds = xr.open_dataset("reference::virtual_store/vstore.parquet", engine="zarr", consolidated=False)
# print(ds)

# Test multiple stores by compression type:
ds1 = xr.open_dataset(
    "reference::virtual_store/vstore1.parquet", engine="zarr", consolidated=False
)
ds2 = xr.open_dataset(
    "reference::virtual_store/vstore2.parquet", engine="zarr", consolidated=False
)
# print(ds1["time"])
# print(ds2["time"])
ds1["T2M"].isel(time=0).plot()
plt.show()
