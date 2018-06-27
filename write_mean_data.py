#!/usr/bin/env python
## code that writes ensemble means at a specific time for each day over a period of a year to a netcdf file

import numpy as np
import netCDF4 as nc
import ensemble_stats
import file_ops

ensemble_size = 8
n_months = 1
n_days = 31

temp_mean = []
pres_mean = []
humidity_mean = []
wind_mean = []

for m in range(n_months):
    for d in range(n_days):
        temp,pres,humidity,wind = ensemble_stats.calculate_mean(0,0,2014,m+1,d+1,3,ensemble_size)
        
        temp_mean.append(temp)
        pres_mean.append(pres)
        humidity_mean.append(humidity)
        wind_mean.append(wind)

# write means to file

write_mean_netCDF(2014,1,31,temp_mean,pres_mean,humidity_mean,wind_mean)
