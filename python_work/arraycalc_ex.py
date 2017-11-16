#! /usr/bin/python2.7 
#
#Script for NumpyArray Ca;aculations exercise 

import numpy as np
print 'Part One.\nBasic Array Calculations'
a = np.array([range(4),range(10,14)])
print a
b = np.array([2,-1,1,0])
print a*b
print b*a 
b1 = b * 100 #multiply b by 100
b2 = b * 100.0 #multiply by by the floating point number 100.0
print b1,b2 # prints both arrays
print b1 == b2 #are the elements equal?

print 'Part Two.\nArray Comparisions'

arr = np.array(range(10))
print np.less(arr,3)
print arr < 3 

condition = np.logical_or( arr > 8, arr < 3 )
c = np.where(condition, arr*5,arr * -5 )
print c

print 'Part Three.\nImplementing mathematical functions on arrays'

def mag_calc(u,v, minmag):
    mag = (u ** 2 + v **2)**0.5
    output = np.where(mag < minmag, minmag,mag)
    return output 

minmag= 0.1
u = np.array([[4,5,0.01],[2,3,4]])
v = np.array([[2,2,0.03],[1,1,1]])

print mag_calc(u,v,minmag)



