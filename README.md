# metoffice_mini_project

All data is read and written for a single grid point - used for condensing data

# write_main_data.py :
  performs ensemble averages of first 8 ensembles for a selected year, month and time of day
  reads test data of remaining 4 ensembles
  
  writes above to file

# file_ops.py:

  contains functions that reads mogreps data and writes data to file
  
  make_data_object_name creates the name for the mogreps files
  write_mean_netCDF writes ensemble means to a netcdf file for a selected month
  read_test_data reads the remaining ensembles from the mogreps files
  write_test_data writes the test data to file

# ensemble_stas.py:

  calculates ensemble averages
