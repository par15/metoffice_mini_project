# README

## Code for reading and condensing mogreps data

### write_local_data.py

Master python source code for writing data for a single grid point to netcdf file. It reads air temperature, relative humidity, surface air pressure and wind speed from the mogreps data for a specified time of day each day for a month, calculates ensemble averages for a 'ensemble_size' realisations, then writes to file.

### write_regional_data.py

Master python source code for writing data averaged over a specified region to netcdf file. It reads air temperature, relative humidity, surface air pressure and wind speed from the mogreps data for a specified time of day each day for a month, calculates ensemble averages for a 'ensemble_size' realisations, then writes to file.

### ensemble_data.py

* ensemble_mean:

Calculates ensemble mean from the mogreps data

* ensemble_regional_mean:

Calculates ensemble regional mean from the mogreps data

### file_ops.py

* make_data_object_name

Finds the appropriate mogreps data file

* write_mean_netCDF

Writes ensemble means to a netcdf file

* read_test_data

Read test data from the mogreps file

* write_test_data

Write test data to a netcdf file

* write_regonal_ensemble_netCDF

Write regional and ensemble averages to a netcdf file

* write_regional_test_data

Write regionally averaged test data to a netcdf file

* read_regional_test_data

Read regional test data from the mogreps file


