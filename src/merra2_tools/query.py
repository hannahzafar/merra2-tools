"""
Input args to query for relevant MERRA-2 files
Refer to MERRA-2 File Specification
MERRA-2 data are organized into collections: freq_dims_group_HV
"""

import numpy as np
import argparse

#TODO: Move these to a utils function
# Function to print for debugging
def print_special(*lists):
    for list in lists:
        print(*list, sep="\n")

def print_val_and_type(item):
    print(f"{item} ({type(item)})")

# Function to parse MERRA2 collection arguments
def MERRA2_parser():
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

    year_list = np.arange(1980,2026)
    parser.add_argument('start_yr',
                        metavar='start_yr',
                        type=int,
                        choices=year_list,
                        help = f"Start Year ({year_list[0]}-{year_list[-1]})",
                        )
    parser.add_argument('end_yr',
                        metavar='end_yr',
                        type=int,
                        choices=year_list,
                        nargs="?",
                        help = f"End Year ({year_list[0]}-{year_list[-1]}), defaults to start_yr",
                        )

    return parser


# Function to find MERRA2 files based on args
def find_MERRA2_files(dir, freq1, freq2, group, start_yr, end_yr):
    #TODO: Check dir is a path obj:

    # Import parser and get args from inputs
    parser = MERRA2_parser()
    argslist = [freq1, freq2, group, start_yr, end_yr]
    args = parser.parse_args(argslist)

    freqF = str(args.freq1) + str(args.freq2)

    #FIX: This no longer works to have optional end year
    # if args.end_yr is None:
    #     args.end_yr=args.start_yr


    # Hard code other vars:
    HV = 'Nx'

    years = [str(year) for year in range(args.start_yr, (args.end_yr)+1)] 

    flist = []
    for year in years:
        pattern = f"Y{year}/M*/MERRA2.{freqF}_2d_{args.group}_{HV}.*.nc4"
        filenames = list(sorted(dir.glob(pattern)))
        flist = flist + filenames

    return flist

