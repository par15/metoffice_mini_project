#!/usr/bin/env python

import netCDF4 as nc
import numpy as np
import file_ops

def calculate_mean(lat,lon,year,month,day,hour,ensemble_size):
    
    #from pathlib import Path
    
    temp_mean = 0.
    pres_mean = 0.
    humidity_mean = 0.
    wind_mean = 0.
    
    for i in range(ensemble_size):
        
        file_name = file_ops.make_data_object_name('mogreps-uk',year,month,day,hour,i,3)

        print(file_name)
        dataset = nc.Dataset(file_name,'r')
        
        
        # read temperature
        
        temp = dataset.variables['air_temperature'][0,0,lat,lon]
        
        # read pressure
        
        pressure = dataset.variables['surface_air_pressure'][0,lat,lon]
        
        # read humidity
        
        humidity = dataset.variables['relative_humidity'][0,0,lat,lon]
        
        # read wind_speed
        
        u_wind = dataset.variables['x_wind'][0,0,lat,lon]
        
        v_wind = dataset.variables['y_wind'][0,0,lat,lon]
        
        wind_speed = np.sqrt(u_wind**2 + v_wind**2)
        
        # close file
        
        dataset.close()
        
        # calculate means
        
        temp_mean = temp_mean + temp
        pres_mean = pres_mean + pressure
        humidity_mean = humidity_mean + humidity
        wind_mean = wind_mean + wind_speed
        

    # normalise mean
    
    temp_mean = temp_mean/ensemble_size
    pres_mean = pres_mean/ensemble_size
    humidity_mean = humidity_mean/ensemble_size
    wind_mean = wind_mean/ensemble_size
    
    return temp_mean, pres_mean, humidity_mean, wind_mean
