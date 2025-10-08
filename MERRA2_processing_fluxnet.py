#!/usr/bin/env python
# Script used to process MERRA-2 data for fluxnet analysis. Modified from processing for GEOS-S2S

import numpy as np
import xarray as xr
import argparse
import glob
import sys

# Debugging function to print
def print_special(*lists):
    for list in lists:
        print(*list, sep="\n")

# Refer to MERRA-2 File Specification
# MERRA-2 data are organized into collections: freq_dims_group_HV
parser = argparse.ArgumentParser(description="User-specified parameters")


freq1list = ["cnst", "inst", "stat", "tavg"] # constant, instantaneous, statistics, timeaveraged 
parser.add_argument('freq1',
                    metavar='freq1',
                    type=str,
                    choices=freq1list,
                    help = f"MERRA-2 Collection Frequency 1 ({', '.join(freq1list)})",
                    )

freq2list = ["1", "3", "6", "M", "D", "U", "0"] # Hourly, 3-Hourly, 6-Hourly, Monthly mean, Daily value, Monthly-Diurnal Mean, Not Applicable
parser.add_argument('freq2',
                    metavar='freq2',
                    type=str,
                    choices=freq2list,
                    help = f"MERRA-2 Collection Frequency 2 ({', '.join(freq2list)})",
                    )
# Variables organized within collections
grouplist = ['slv', 'asm', 'flx']
parser.add_argument('group',
                    metavar='ggg',
                    type=str,
                    choices=grouplist,
                    help = f"MERRA-2 Collection Group ({', '.join(grouplist)})",
                    )

# year_list = np.arange(1980,2026)
# parser.add_argument('start_yr',
#                     metavar='start_yr',
#                     type=int,
#                     choices=year_list,
#                     help = f"Start Year ({year_list[0]}-{year_list[-1]})",
#                     )
# parser.add_argument('end_yr',
#                     metavar='end_yr',
#                     type=int,
#                     choices=year_list,
#                     nargs="?",
#                     help = f"End Year ({year_list[0]}-{year_list[-1]}), defaults to start_yr",
#                     )

varlist = ["T2M", "T10M" ,"PRECTOT"]
# Should I make this as many inputs as you want?
parser.add_argument('--vars',
                    metavar='var',
                    type=str,
                    required=True,
                    nargs='+',
                    choices=varlist,
                    help = f"MERRA-2 Variable(s) ({', '.join(varlist)})",
                    )

args = parser.parse_args()
freqF = str(args.freq1) + str(args.freq2)
group = args.group

# start_yr = args.start_yr
# if args.end_yr is None:
#     args.end_yr=args.start_yr
# end_yr = args.end_yr

var = args.vars
#TODO: Ideally this would check if these vars are valid in that collection group

# print(freqF, group, start_yr, end_yr, var) #Note that now var is a list, but we can just loop over it right?

# Hard code the rest:
HV = 'Nx'
dir = '/discover/nobackup/hzafar/MERRA2_processing/MERRA2_all' # Made a new symlink to MERRA-2 data


#NOTE: How am I going to select years? If Amerflux varies? Similar to MiCASA I suppose, or should I look at all the years I have a record from and average across long time series??? 
# AmeriFlux FLUXNET spans 1991-2021 across all the sites, individual sites vary, let's just start with thisk
start_yr, end_yr = [1991, 2021]
years = [str(year) for year in range(start_yr, end_yr+1)] 

flist = []
for year in years:
    filenames = sorted(glob.glob(f"{dir}/Y{year}/M*/MERRA2.{freqF}_2d_{group}_{HV}.*.nc4"))
    flist = flist + filenames
# print_special(flist[:10],flist[-10:])

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

# This is all old from prev code
# ds_MERRA2 = ds_MERRA2.to_dataframe()
# ds_MERRA2.index = ds_MERRA2.index.normalize() #This gets rid of the 30 min time stamp?
# filename = 'MERRA2_extract_'+ var + '_' + POLE  + '.csv'
# path = 'transfer/' + filename
# ds_MERRA2.to_csv(path)
# print('Dataset written to .csv file')


