#! /usr/bin/python
# Sctipry for the Strings exercise 

print 'Part One. \nLooping through a string'
s = 'I love to write python...'
for char in s: #loop through each letter in s and print it to terminal
    print char

print 'print the 5th element, the last element and string length'
print s[5], s[-1], len(s)

print 'print s[0]:', s[0]
print 'print s[0][0]:',s[0][0]
print 'print s[0][0][0]:', s[0][0][0]

print 'Part Two. \n Splitting a string.'

s = 'I still love to write python...'

s_split = s.split(' ')
print s_split

for word in s_split:
    if word.find('i')  != -1: # If i is not found then find returns -1
         print 'I found \'i\' in: \'{0}\'!! {1}'.format(word, 'hooray')

print 'Part Three. \n Other useful aspects of strings'

something = 'Completely Different'

print dir(something) #prints all properties and methods for the string

ct = something.count('t')
fd = something.find('plete')
print "There are {0} instances of 't' in the string and the string 'plete' starts at {1}".format(ct,fd) 

sp = something.split('e')
print sp

thing2 = something.replace('Different','Silly')
print thing2

