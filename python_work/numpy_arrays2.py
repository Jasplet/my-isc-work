#! /usr/bin/python2.7
import numpy as np 
#Interrogating and Manipulating Arrays

print 'Part One.\nInterrogation\n'

arr = np.array([range(4),range(10,14)])
print 'The array arr = ', arr
print 'The shape of arr is :', np.shape(arr) #Returns dimensions of array
print 'The size of arr is:', np.size(arr) #Returns the number of elements in the array
print 'The mininum value is: ', np.min(arr),'\nThe maximum value is: ',np.max(arr)

print'Part Two.\nModifying Arrays'

print np.reshape(arr,(2,2,2)) # Reshapes the array to a 2x2x2 3-D array

np.transpose(arr) #Transposes the array 

print np.ravel(arr)

print arr.astype(np.float64)
