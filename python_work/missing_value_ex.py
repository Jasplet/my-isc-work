#! /usr/bin/python2.7
# Working with Missing Values exercise
import numpy as np
import numpy.ma as MA

a = MA.masked_array(range(10),fill_value = float('NaN'),dtype=np.float32) # create a masked array with 
print a, a.fill_value # Fill value for this mask is Nan (not a number)

a[3] = MA.masked

print 'Now its masked the array looks like this:',a,'\nThe mask itself is:',a.mask

b = MA.masked_where(a >= 7, a )
print b 
print b.fill_value
c = MA.filled(b)
print c

print 'Part Two.\nA mask that is smaller than the array'
m1 = MA.masked_array(range(1,9),fill_value = -999)
m2 = m1.reshape(2,4)
print m2
m3 = MA.masked_where( m2 >6,m2)
print m3 

print 'Extra examples I made'

d = np.array(range(5,15))
print d
e = np.array(range(0,20,2))
print e
print 'You can set a mask based on a condition which compares to another array!\nFirst lets mask values in d which are greater than e'
d2 = MA.masked_where(d > e, d)
print d2
print 'Lets see if we can masked array based on a condition which is not directly related to it!'
d3 = MA.masked_where(e > 13, d)
print d3 
