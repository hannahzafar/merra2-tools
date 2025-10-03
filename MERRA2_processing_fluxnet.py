#!/usr/bin/env python
# Script used to process MERRA-2 data for fluxnet analysis. Modified from processing for GEOS-S2S

import xarray as xr
import argparse
import glob

parser = argparse.ArgumentParser(description="User-specified parameters")

# MERRA-2 data are organized into collections: freq_dims_group_HV
freq1list = ["cnst", "inst", "stat", "tavg"] # constant, instantaneous, statistics, timeaveraged 
parser.add_argument('freq1',
                    metavar='freq',
                    type=str,
                    choices=freq1list,
                    help = f"MERRA-2 Collection Frequency 1 ({', '.join(freq1list)})",
                    )

freq2list = ["1", "3", "6", "M", "D", "U", "0"] # Hourly, 3-Hourly, 6-Hourly, Monthly mean, Daily value, Monthly-Diurnal Mean, Not Applicable
parser.add_argument('freq2',
                    metavar='F',
                    type=str,
                    choices=freq2list,
                    help = f"MERRA-2 Collection Sub-frequency ({', '.join(freq2list)})",
                    )
# Each collection has certain variables
grouplist = ['slv', 'asm', 'flx']
parser.add_argument('group',
                    metavar='ggg',
                    type=str,
                    choices=grouplist,
                    help = f"MERRA-2 Collection Group ({', '.join(grouplist)})",
                    )

varlist = ["T2M", "PRECTOT"]
# Should I make this as many inputs as you want?
# Can I just dump out the T2M daily for every lat/lon of each flux site for the years I am concerned with? Look into what years I have
parser.add_argument('var',
                    metavar='VAR',
                    type=str,
                    nargs='+',
                    choices=varlist,
                    help = f"MERRA-2 Variable(s) ({', '.join(varlist)})",
                    )

args = parser.parse_args()
freqF = str(args.freq1) + str(args.freq2)
VAR = args.var
print(freqF, VAR) #Note that now VAR is a list, but we can just loop over it right?

# Hard code the rest:
HV = 'Nx'
DIR = '/discover/nobackup/hzafar/MERRA2_processing/MERRA2_all' # Made a new symlink to MERRA-2 data

#TODO: add an arg for FREQ (tavgM) Actually I think everything is tavg M, since before I was using monthly means and now I need to do annual so I will have to select from the monthly and average. What's different is the N/S, now I want the specific lat/lon of the sites. So maybe change that arg around 
#NOTE: How am I going to select years? If Amerflux varies? Similar to MiCASA I suppose, or should I look at all the years I have a record from and average across long time series??? 

start_yr, end_yr = [1990, 2010]
years = [str(year) for year in range(start_yr, end_yr+1)] 


####### SLP ####################################
if VAR=='SLP':
    flist = []
    for year in years:
        fnames = sorted(glob.glob( DIR+'/Y' + str(year) +'/M*/MERRA2.tavgM_2d_slv_Nx.*.nc4')) # Uses glob function, beware
        flist= flist + fnames

    ds_MERRA2 = xr.open_mfdataset(flist,parallel=True, chunks = {'time':10})[VAR]
    if POLE == 'N':
        ds_MERRA2 = ds_MERRA2.where(ds_MERRA2.lat>=60,drop=True).mean(dim=["lat","lon"])
    else:
        ds_MERRA2 = ds_MERRA2.where(ds_MERRA2.lat<=-60,drop=True).mean(dim=["lat","lon"])

    ds_MERRA2 = ds_MERRA2.to_dataframe()
    ds_MERRA2.index = ds_MERRA2.index.normalize() #This gets rid of the 30 min time stamp?
    filename = 'MERRA2_extract_'+ VAR + '_' + POLE  + '.csv'
    path = 'transfer/' + filename
    ds_MERRA2.to_csv(path)
    print('Dataset written to .csv file')


