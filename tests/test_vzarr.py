#!/usr/bin/env python
# Test create_vzarr_store function
# Contains old notes used to process MERRA-2 data for fluxnet analysis


from merra2_tools import MERRA2_ROOT, find_MERRA2_files, create_vzarr_store

#NOTE: How am I going to select years, if Amerflux years varies across sites?
# AmeriFlux FLUXNET spans 1991-2021 across all the sites, individual sites vary, let's just start with that
start_yr, end_yr = [2014, 2017]
freq1 = "tavg"
freq2 = "M"
group = "slv"

fileslist = find_MERRA2_files(MERRA2_ROOT, freq1, freq2, group, str(start_yr), str(end_yr))

# vstore_loc = create_vzarr_store(fileslist)
# print(vstore_loc)
create_vzarr_store(fileslist)

### DEBUGGING ####

# file_name = "test_file_list.txt"
# with open(file_name, "w") as file:
#     for item in fileslist:
#         file.write(str(item) + "\n")

# import h5netcdf
#
# file_name = "test_file_datetimes.txt"
# with open(file_name, "w") as file:
#     for fpath in fileslist:
#         with h5netcdf.File(fpath, "r") as f:
#             v = f.variables["time"]
#             info = f"{fpath}: dtype={v.dtype}, units={v.attrs.get('units')}, calendar={v.attrs.get('calendar')}"
#             file.write(info + "\n")

# import netCDF4
# from netCDF4 import Dataset
#
# file_name = "test_file_codec.txt"
# with open(file_name, "w") as file:
#     for fpath in fileslist:
#         with Dataset(fpath, "r") as ds:
#             for vname, var in ds.variables.items():
#                 info = f"{fpath} {vname}: zlib={getattr(var.filters(), 'zlib', 'None')}, filters={getattr(var.filters(), 'shuffle', 'None')}"
#                 file.write(info + "\n")
        # with h5netcdf.File(fpath, "r") as f:
        #     for vname, v in f.variables.items():
        #         # info = f"{fpath} {vname}: {v.encoding.get("filters", "None")}"
        #         info = f"{fpath} {vname}"
        #     break

import h5py

def get_codecs(path, var_name="T2M"):
    with h5py.File(path, "r") as f:
        if var_name not in f:
            return "missing"
        dset = f[var_name]
        # Compression name is 'gzip' for zlib, or None if uncompressed
        return f"compression={dset.compression}, shuffle={dset.shuffle}"

for file in fileslist:
    print(file.name, get_codecs(file))
