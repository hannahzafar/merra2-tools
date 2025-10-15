#!/usr/bin/env python
# Test find_MERRA2_files function


from merra2_tools import MERRA2_ROOT, find_MERRA2_files
from merra2_tools import print_val_and_type as print_special

start_yr, end_yr = [2020, 2021]
freq1 = "tavg"
freq2 = "M"
group = "slv"
varslist = ["T2M", "T10M" ,"PRECTOT"] # vars should work as a list now
vars = varslist[0]

fileslist = find_MERRA2_files(MERRA2_ROOT, freq1, freq2, group, str(start_yr), str(end_yr))
print_special(fileslist[0])
for file in fileslist:
    print(str(file))

