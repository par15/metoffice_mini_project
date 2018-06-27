#!/usr/bin/env python

def make_data_object_name(
        dataset_name,
        year, month, day, hour,
        realization, forecast_period):
    """Create a string formatted to give a filename in the MOGREPS dataset."""
    template_string = "mogreps_data/prods_op_{}_{:02d}{:02d}{:02d}_{:02d}_{:02d}_{:03d}.nc"
    return template_string.format(
        dataset_name, year, month, day, hour, realization, forecast_period)

def write_mean_netCDF(year,month,no_days,temp_mean, pres_mean, humidity_mean, wind_mean):
    
    template_string ="ensemble_means_{:02d}{:02d}.nc"
    
    file_name = template_string.format(
        year, month)
    
    dataset = nc.Dataset(file_name,'w')
    
    
    dataset.createDimension('Days',no_days)
    
    temp_var = dataset.createVariable('Temperature',np.float32,('Days'))
    pres_var = dataset.createVariable('Pressure',np.float32,('Days'))
    humidity_var = dataset.createVariable('Humidity',np.float32,('Days'))
    wind_var = dataset.createVariable('Wind Speed',np.float32,('Days'))
    
    temp_var[:no_days] = temp_mean
    pres_var[:no_days] = pres_mean
    humidity_var[:no_days] = humidity_mean
    wind_var[:no_days] = wind_mean
    
    dataset.close()
    
    return
