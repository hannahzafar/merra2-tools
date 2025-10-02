#!/usr/bin/env python
# Script used to process MERRA-2 data on discover for other analysis

import numpy as np
import xarray as xr
import argparse

parser = argparse.ArgumentParser(description="User-specified parameters")
polelist = ['N', 'S']
parser.add_argument('pole',
                    metavar='P',
                    type=str, 
                    choices=polelist,
                    help = f"Pole ({', '.join(polelist)})",
                    )

varlist = ["SLP", "PRECSNO", "TS"]
parser.add_argument('var',
                    metavar='var',
                    type=str,
                    choices=varlist,
                    help = f"MERRA-2 Variable ({', '.join(varlist)})",
                    )
args = parser.parse_args()
POLE = args.pole
VAR = args.var

DIR = '/discover/nobackup/hzafar/MERRA2_processing/MERRA2_all' # Made a new symlink to MERRA-2 data
start_yr, end_yr = [1990, 2010]
years = [str(year) for year in range(start_yr, end_yr+1)] 
months_mm = [f"{i:02d}" for i in range(1, 13)]

####### SLP ####################################
var_name = 'SLP'
vars = [var_name]
############# ALL MONTHS
flist = []
for year in years:
  for mon in months:
    mon_str=str(mon)
    if mon < 10: 
        mon_str ='0'+mon_str
    fname = DIR+'/Y'+str(year)+'/M'+mon_str+'/MERRA2.tavgM_2d_slv_Nx.'+str(year)+mon_str+'.nc4'
    flist.append(fname)

ds_MERRA2 = xr.open_mfdataset(flist,parallel=True, chunks = {'time':10})[vars]
if POLE == 'N':
    ds_MERRA2 = ds_MERRA2.where(ds_MERRA2.lat>=60,drop=True).mean(dim=["lat","lon"])
else:
    ds_MERRA2 = ds_MERRA2.where(ds_MERRA2.lat<=-60,drop=True).mean(dim=["lat","lon"])

ds_MERRA2 = ds_MERRA2.to_dataframe()
ds_MERRA2.index = ds_MERRA2.index.normalize()

filename = 'MERRA2_extract_'+ var_name + '_' + POLE  + '.csv'
path = 'transfer/'+filename
ds_MERRA2.to_csv(path)
print('Dataset written to .csv file')

########### SEASONAL MAX/MIN ONLY (OLD)
#if POLE == 'N':
#  SEASON=['M03', 'M09']
#  MONTH=['MAR', 'SEP']
#else:
#  SEASON=['M09', 'M02']
#  MONTH=['SEP', 'FEB']
#
#flist = []
#for year in years:
#  for i, (sea,mon) in enumerate(zip(SEASON,MONTH)):
#    fname = DIR+'/Y'+str(year)+'/'+sea+'/MERRA2.tavgM_2d_slv_Nx.'+str(year)+sea[-2:]+'.nc4'
#    flist.append(fname)
#
#ds_MERRA2 = xr.open_mfdataset(flist,parallel=True)[vars]
#    
#if POLE == 'N':
#    ds_MERRA2 = ds_MERRA2.where(ds_MERRA2.lat>=60,drop=True).mean(dim=["lat","lon"])
#else:
#    ds_MERRA2 = ds_MERRA2.where(ds_MERRA2.lat<=-60,drop=True).mean(dim=["lat","lon"])
#
#ds_MERRA2 = ds_MERRA2.to_dataframe()
#filename = 'MERRA2_extract_sea'+ var_name + '_' + POLE  + '.csv'
#path = 'transfer/'+filename
#ds_MERRA2.to_csv(path)
#print('Dataset written to .csv file')

############ SNOWFALL############
var_name = 'PRECSNO'
vars = [var_name]

############ ALL MONTHS
flist = []
for year in years:
  for mon in months:
    mon_str=str(mon)
    if mon < 10:
        mon_str ='0'+mon_str
    fname = DIR+'/Y'+str(year)+'/M'+mon_str+'/MERRA2.tavgM_2d_flx_Nx.'+str(year)+mon_str+'.nc4'
    flist.append(fname)

ds_MERRA2 = xr.open_mfdataset(flist,parallel=True)[vars]
    
if POLE == 'N':
    ds_MERRA2 = ds_MERRA2.where(ds_MERRA2.lat>=60,drop=True).mean(dim=["lat","lon"])
else:
    ds_MERRA2 = ds_MERRA2.where(ds_MERRA2.lat<=-60,drop=True).mean(dim=["lat","lon"])

ds_MERRA2 = ds_MERRA2.to_dataframe()
ds_MERRA2.index = ds_MERRA2.index.normalize()

filename = 'MERRA2_extract_'+ var_name + '_' + POLE  + '.csv'
path = 'transfer/'+filename
ds_MERRA2.to_csv(path)
print('Dataset written to .csv file')




############ SKIN TEMP###########
var_name = 'TS'
vars = [var_name]

############ ALL MONTHS
flist = []
for year in years:
  for mon in months:
    mon_str=str(mon)
    if mon < 10:
        mon_str ='0'+mon_str
    fname = DIR+'/Y'+str(year)+'/M'+mon_str+'/MERRA2.tavgM_2d_slv_Nx.'+str(year)+mon_str+'.nc4'
    flist.append(fname)
###print(flist)
ds_MERRA2 = xr.open_mfdataset(flist,parallel=True)[vars]
    
if POLE == 'N':
    ds_MERRA2 = ds_MERRA2.where(ds_MERRA2.lat>=60,drop=True).mean(dim=["lat","lon"])
else:
    ds_MERRA2 = ds_MERRA2.where(ds_MERRA2.lat<=-60,drop=True).mean(dim=["lat","lon"])

ds_MERRA2 = ds_MERRA2.to_dataframe()
ds_MERRA2.index = ds_MERRA2.index.normalize()

filename = 'MERRA2_extract_'+ var_name + '_' + POLE  + '.csv'
path = 'transfer/'+filename
ds_MERRA2.to_csv(path)
print('Dataset written to .csv file')


