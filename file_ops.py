#!/usr/bin/env python

def make_data_object_name(
		dataset_name,
        year, month, day, hour,
        realization, forecast_period):
    """Create a string formatted to give a filename in the MOGREPS dataset."""
    template_string = "mogreps_data/prods_op_{}_{:02d}{:02d}{:02d}_{:02d}_{:02d}_{:03d}.nc"
    return template_string.format(
        dataset_name, year, month, day, hour, realization, forecast_period)

def write_mean_netCDF(lat,lon,year,month,no_days,temp_mean, pres_mean, humidity_mean, wind_mean):

## write the local ensemble means to a netcdf file

    import netCDF4 as nc
    import numpy as np
    
    template_string ="ensemble_mean_data/ensemble_means_{:02d}{:02d}_lat{:03d}_lon{:03d}.nc"
    
    file_name = template_string.format(
        year, month, lat, lon)
    
    dataset = nc.Dataset(file_name,'w')
    
    dataset.createDimension('Days',no_days)
    
    temp_var = dataset.createVariable('Temperature',np.float32,('Days'))
    pres_var = dataset.createVariable('Pressure',np.float32,('Days'))
    humidity_var = dataset.createVariable('Humidity',np.float32,('Days'))
    wind_var = dataset.createVariable('Wind Speed',np.float32,('Days'))
    
    temp_var[:] = temp_mean
    pres_var[:] = pres_mean
    humidity_var[:] = humidity_mean
    wind_var[:] = wind_mean
    
    dataset.close()
    
    return

def read_test_data(lat,lon,year,month,day,hour,test_size):

# read the test data, that is, the ensemble members that haven't been trained on
    
    import netCDF4 as nc
    import numpy as np

    temp_test = []
    pressure_test = []
    humidity_test = []
    wind_test = []

    for i in range(test_size):

        mogreps_data = make_data_object_name('mogreps-uk',year,month,day,hour,11-i,3)
        print(mogreps_data)
        dataset = nc.Dataset(mogreps_data,'r')

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
	
		# append test data

        temp_test.append(temp)
        pressure_test.append(pressure)
        humidity_test.append(humidity)
        wind_test.append(wind_speed)

        
        # close file
        
        dataset.close()

    return temp_test,pressure_test,humidity_test,wind_test

def write_test_data(lat,lon,year,month,n_days,hour,test_size):

## write test data to a netcdf file
    
    import netCDF4 as nc
    import numpy as np

    temp_test = np.zeros((n_days,test_size))
    pressure_test = np.zeros((n_days,test_size))
    humidity_test = np.zeros((n_days,test_size))
    wind_test = np.zeros((n_days,test_size))

    for d in range(n_days):

		# read test data

        temp_test[d,:],pressure_test[d,:],humidity_test[d,:],wind_test[d,:] = read_test_data(lat,lon,year,month,d+1,hour,test_size)

	# name file

    template_string ="test_data/test_data_{:02d}{:02d}_lat{:03d}_lon{:03d}.nc"
    
    file_name = template_string.format(
        year, month, lat, lon)
    dataset = nc.Dataset(file_name,'w')

	# create dimensions

    dataset.createDimension('Days',n_days)
    dataset.createDimension('Ensemble Number',test_size)

 	# create variables

    temp_var = dataset.createVariable('Temperature',np.float32,('Days','Ensemble Number'))
    pres_var = dataset.createVariable('Pressure',np.float32,('Days','Ensemble Number'))
    humidity_var = dataset.createVariable('Humidity',np.float32,('Days','Ensemble Number'))
    wind_var = dataset.createVariable('Wind Speed',np.float32,('Days','Ensemble Number'))

	# write to variables

    temp_var[:] = temp_test
    pres_var[:] = pressure_test
    humidity_var[:] = humidity_test
    wind_var[:] = wind_test

    dataset.close()


    return

def write_regional_ensemble_netCDF(year,month,n_days,temp_mean,pres_mean,humidity_mean,wind_mean):

## write a netcdf file containing regional ensemble means

    import netCDF4 as nc
    import numpy as np
    
    template_string ="ensemble_mean_data/ensemble_regional_means_{:02d}{:02d}.nc"
    
    file_name = template_string.format(
        year, month)
    
    dataset = nc.Dataset(file_name,'w')
    
    dataset.createDimension('Days',n_days)
    
    temp_var = dataset.createVariable('Temperature',np.float32,('Days'))
    pres_var = dataset.createVariable('Pressure',np.float32,('Days'))
    humidity_var = dataset.createVariable('Humidity',np.float32,('Days'))
    wind_var = dataset.createVariable('Wind Speed',np.float32,('Days'))
    
    temp_var[:] = temp_mean
    pres_var[:] = pres_mean
    humidity_var[:] = humidity_mean
    wind_var[:] = wind_mean
    
    dataset.close()

    return

def write_regional_test_data(lat_start,lat_end,lon_start,lon_end,year,month,n_days,hour,test_size):

## write a netcdf file containing regional test data
    
    import netCDF4 as nc
    import numpy as np

    temp_test = np.zeros((n_days,test_size))
    pressure_test = np.zeros((n_days,test_size))
    humidity_test = np.zeros((n_days,test_size))
    wind_test = np.zeros((n_days,test_size))

    for d in range(n_days):

		# read test data

        temp_test[d,:],pressure_test[d,:],humidity_test[d,:],wind_test[d,:] = read_regional_test_data(lat_start,lat_end,lon_start,lon_end,year,month,d+1,hour,test_size)

	# name file

    template_string ="test_data/regional_test_data_{:02d}{:02d}.nc"
    
    file_name = template_string.format(
        year, month)
    dataset = nc.Dataset(file_name,'w')

	# create dimensions

    dataset.createDimension('Days',n_days)
    dataset.createDimension('Ensemble Number',test_size)

 	# create variables

    temp_var = dataset.createVariable('Temperature',np.float32,('Days','Ensemble Number'))
    pres_var = dataset.createVariable('Pressure',np.float32,('Days','Ensemble Number'))
    humidity_var = dataset.createVariable('Humidity',np.float32,('Days','Ensemble Number'))
    wind_var = dataset.createVariable('Wind Speed',np.float32,('Days','Ensemble Number'))

	# write to variables

    temp_var[:] = temp_test
    pres_var[:] = pressure_test
    humidity_var[:] = humidity_test
    wind_var[:] = wind_test

    dataset.close()


    return

def read_regional_test_data(lat_start,lat_end,lon_start,lon_end,year,month,day,hour,test_size):

## read the regional test data from the mogreps data
    
    import netCDF4 as nc
    import numpy as np

    temp_test = []
    pressure_test = []
    humidity_test = []
    wind_test = []

    for i in range(test_size):

        mogreps_data = make_data_object_name('mogreps-uk',year,month,day,hour,11-i,3)
        #print(mogreps_data)
        dataset = nc.Dataset(mogreps_data,'r')

        # read temperature
        
        temp = np.mean(dataset.variables['air_temperature'][0,0,lat_start:lat_end,lon_start:lon_end])
        
        # read pressure
        
        pressure = np.mean(dataset.variables['surface_air_pressure'][0,lat_start:lat_end,lon_start:lon_end])
        
        # read humidity
        
        humidity = np.mean(dataset.variables['relative_humidity'][0,0,lat_start:lat_end,lon_start:lon_end])
        
        # read wind_speed
        
        u_wind = np.mean(dataset.variables['x_wind'][0,0,lat_start:lat_end,lon_start:lon_end])
        
        v_wind = np.mean(dataset.variables['y_wind'][0,0,lat_start:lat_end,lon_start:lon_end])
        
      	wind_speed = np.sqrt(u_wind**2 + v_wind**2)
	
		# append test data

        temp_test.append(temp)
        pressure_test.append(pressure)
        humidity_test.append(humidity)
        wind_test.append(wind_speed)

        
        # close file
        
        dataset.close()

    return temp_test,pressure_test,humidity_test,wind_test
