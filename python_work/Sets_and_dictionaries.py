#! /usr/bin/python2.7
## Script for exercise on Sets and Dictionaries
print 'Part One. \nCreating and working with sets'
a = set([0,1,2,3,4,5]) # create a set using the standard python 2.6 method
b = {2,4,6,8} # Creast another set using the new {} method

print a.union(b) # pritn a union of the two sets

print a.intersection(b) # Prints values in common for the two sets { 2,4}

print 'Part Two. \nCollecting counts in a Dictionary'

band = ['mel','geri','victoria','mel','emma']

counts = dict()

for member in band:
    if member in counts:
         counts[member] += 1 
    else:
         counts[member] = 1
print counts

for member in counts:
    print member, counts[member]

print 'Part Three \nLooking at other properties of dictionaries'

if {}: # Is and empty dictionary evaluated at True by python?
    print 'Hi' # 'Hi' did not print so no

d = {'maggie':'uk','ronnie':'usa'}
print dir(d) #print methods of the dictionary

print d.items() # Prints items in dictionary
print d.keys() # Returns keys as a list
print d.values() # Returns values as a list

print d.get('fred', 'uk') # d.get searches the dictionary for the first arguement. If it is in the dictionary then its value is returned. If not then the second(optional) arguement will be returned. If there is only one arguement (and its not in the dictionary) then None is returned
print d.get('maggie','france')
print d.get('Ben')
print d.setdefault('francois','france')  # Similar to get, BUT if the key is not in your dictionary then is is added to the dictionary. Only one arguemnt is needed but two will be accepted. 
print d.setdefault('Karl')
print d

