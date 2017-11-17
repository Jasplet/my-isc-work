#! /usr/bin/python2.7
## Script for netCDF exercise

import netCDF4 as net ## Import netCDF module

ds = net.Dataset('example_data/ggas2014121200_00-18.nc')

# Lets loop through and print the variable so we know what they are
for v in ds.variables: 
    print v

sst = ds.variables['SSTK']
print sst 

for dim in sst.dimensions:
    print dim, len(dim)

print 'The variable SST has shape:',sst.shape,'\nand has size:', sst.size 

for att in sst.ncattrs():
    print att,'=',getattr(sst,att)


print 'Part Two\n Extracting Data'

arr = sst[1,0,10:20,30:35]

print type(arr) # arr is a masked array!

dims = sst.dimensions #dimensions of SST
print dims

vars = ds.variables
arr_time = vars['time'][1] #assigning variables to new arrays
arr_level = vars['surface'][0]
arr_lats = vars['latitude'][10:20]
arr_lons = vars['longitude'][30:35]

for vals in (arr_time,arr_level,arr_lats,arr_lons): #loop over these 4 new variables to print values
    print vals

metadata = {}
for attr in sst.ncattrs():
    metadata[attr] = getattr(sst,attr)

print metadata



