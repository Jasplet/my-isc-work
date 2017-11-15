#! /usr/bin/python
# Tuples Exercise 

print 'Part Four. \n'

t = 1, #Example of a one integer Tuple
print "The last element of t is: ", t[-1]

a = range(100,201)
tup = tuple(a)
print 'The first element of 100 element tuple is:',tup[0], 'and the last is:', tup[-1]

print 'Part Two. \n Using Enumerate  \n'
mylist  = [23,'hi',2.4e-10]
for (index,item) in enumerate(mylist):
    print index, item 

print 'Part Three \n Unpacking values from a list of a tuple \n'

(first,middle,last) = mylist #tuple unpakcing mylist into 3 variables for the first middle and last values

print 'First is:',first,'Second is:',middle,'Third is:', last

(middle,last,first) = first,middle,last # can use tuples to assign multiple variables in an efficient way

print 'After ressasignment. First is:',first,'Second is:',middle,'Third is:', last
