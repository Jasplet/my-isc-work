#! \bin\env python

## The Basics .... Variable and types
# 1.
course = 'python'
rating = 1.0  
# 2. "My First equation in Python"
import math.sqrt as sq #basic module with math functions 
b = 3 
c = 4 

a = sq(b**2 + c**2) # Pythagoras' theorem

# Printing the results

print a, "squared equals", b "squared plus", c "squared!"

## Note that numeric variable default to integer values, as to thier reuslts if we do maths with them!!
# Eg

d = 2
e = 3

print e/d # this will return 1 not 1.5!!

print 3.0/2 # 3.0 is a float so now we will get a float as an output 
