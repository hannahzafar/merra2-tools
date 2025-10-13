#!/usr/bin/env python
# Script used to process MERRA-2 data for fluxnet analysis


from merra2_tools import MERRA2_ROOT, find_MERRA2_files

#NOTE: How am I going to select years, if Amerflux years varies across sites?
# AmeriFlux FLUXNET spans 1991-2021 across all the sites, individual sites vary, let's just start with that
start_yr, end_yr = [1991, 2021]
freq1 = "tavg"
freq2 = "M"
group = "slv"
varslist = ["T2M", "T10M" ,"PRECTOT"] # vars should work as a list now
vars = varslist[0]

fileslist = find_MERRA2_files(MERRA2_ROOT, freq1, freq2, group, str(start_yr), str(end_yr))


