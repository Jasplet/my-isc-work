#! /usr/bin/python 
# This exercise covers Lists and Slicing

print 'Part One. \n'

mylist = range(1,6)
print 'mylist =', mylist

a = mylist[1] #selects second item in the list (indexing starts at 0)
print 'a =', a
b = mylist[-2] # selects second last item in list (indexing from the end starts at -1)
print 'b =', b 
c = mylist[:] # List slicing to select all items in list
print 'c =', c 
d = mylist[2:5]
print 'd =', d 

print 'Part Two.'
# Creating a list from a range .....
one_to_ten = range(1,11)
print one_to_ten, 'A list form one to ten'
one_to_ten[0] = 10 #replaces first element with 10
one_to_ten.append(11)
print one_to_ten, "see how 11 has been appended ( and 0 has been replaced with 10)"
one_to_ten.extend([12,13,14]) #extends the list with the new one 
print one_to_ten, 'now the list has been extended further'

print 'Part Three \n'

forward = []
backward = [] # initialise two empty lists
values = ['a','b','c']

for i in values:
    forward.append(i)
    backward.insert(0,i)

print forward, 'made using append'
print backward, 'made using insert'

forward.reverse()

if forward == backward:
    print('Now they are the same')
    print 'Appended list', forward
    print 'Inserted list', backward

print 'Part Four. \n'

countries = ['uk','usa','uk','uae']
print countries
count  = countries.count('uk')
print 'I can count the uk', count, 'times in the list!' 


