#! /usr/bin/python	

## Script containing work for the second set of exercises "Control Flow"
# Remeber to use 4-space indentations for loops !!
#1. Creating While loops
# Infinite While loop - break added for Sanity!
print "Part One. \n"
a = 1 
while a > 0:
    a += 1
    print a

    if a > 10: 
	break

# An Uncalled while loop

b = 1.0
while b < 1: 
    b = (b + 1)/2
    print b 

else: 
    print "Loop not Called"

print "Part Two. \n"
# Iterating over a list of items
mylist = [23, "hi", 2.4e-10]
count = 0 

while count < 3:
    item = mylist[count]
    print item, mylist.index(item) 
    count += 1

print "Part Three. \n"
# Trying out if statements

name = "Lisa"
if name == "Lisa":
    print name, "plays Saxophone"
elif name == "Bart":
    print name, "rides a Skateboard"
else:
    print name,"Lives in Springfield"

