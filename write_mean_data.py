#!/usr/bin/env python
## code that writes ensemble means at a specific time for each day over a period of a year to a netcdf file

import numpy as np
import netCDF4 as nc
import ensemble_stats
import file_ops

# set variables

ensemble_size = 8
month = 2
year = 2014
hour = 3

# determine correct number of days
if month in [1,3,5,7,8,10,12]:
	n_days = 31
elif month in [4,6,9,11]:
	n_days =30
else:
	n_days = 28

temp_mean = []
pres_mean = []
humidity_mean = []
wind_mean = []

#for d in range(n_days):
#	temp,pres,humidity,wind = ensemble_stats.calculate_mean(0,0,2014,month,d+1,3,ensemble_size)
        
#        temp_mean.append(temp)
#        pres_mean.append(pres)
#        humidity_mean.append(humidity)
#        wind_mean.append(wind)


# write means to file

#file_ops.write_mean_netCDF(year,month,n_days,temp_mean,pres_mean,humidity_mean,wind_mean)

# write test_data to file

test_size = 12 - ensemble_size

file_ops.write_test_data(year,month,n_days,hour,test_size)
