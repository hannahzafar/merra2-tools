#!/usr/bin/env python
# Test create_vzarr_store function


from merra2_tools import MERRA2_ROOT, find_MERRA2_files, create_vzarr_store
import argparse

parser = argparse.ArgumentParser(description="Test inputs")
parser.add_argument("start_yr")
parser.add_argument("end_yr")
args = parser.parse_args()

start_yr = int(args.start_yr)
end_yr = int(args.end_yr)
# start_yr, end_yr = [2014, 2015]
freq1 = "tavg"
freq2 = "M"
group = "slv"

details, fileslist = find_MERRA2_files(
    MERRA2_ROOT, freq1, freq2, group, str(start_yr), str(end_yr)
)

store = create_vzarr_store(details, fileslist)
print(store)
# vstore_loc = create_vzarr_store(details, fileslist)
# print(vstore_loc)

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
