#! /usr/bin/python2.7
#Intro Numpy Exercise
import numpy as np
print 'Part One.\n  Creating Numpy Array\'s'

x = range(1,11)
a1 = np.array(x, np.int32)# create an integer array
a2 = np.array(x,np.float32)  # create an array of floating point numbers
print 'Integer array',a1 ,'\nFloating point array',a2
print 'Part Two.\nOther ways of making arrays'

b0 = np.zeros((2,3,4))
print 'A 3D array of zeros: ', b0
b1 = np.ones((2,3,4))
print 'A 3D array one ones: ', b1
b_eye = np.matrix(np.eye((3)))
print 'An Identity Array(matrix)?', b_eye
print type(b_eye)
 
b999 = np.array([[range(0,10)],[range(10,20)]])
print b999


print 'Part Three.\n Indexing and Slicing'

a = np.array([2,3.2,5.5,-6.4,-2.2,2.4])
print a[1]  #SHould give us 3.2 
print a[1:4] 







