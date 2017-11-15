#! /usr/bin/python 
# This script is for the functions exercise 

print 'Part One. \nCreating a simple function'

def double_it(number):
    if type(number) is str: 
        print 'error'
    else:
        return 2 * number
a = 5
b = double_it(a)
print b

print 'Part Two. \nPythangoras\' Function'

def pythag(a,b):
    accept = (int,float)
    if type(a) in accept and type(b) in accept:
        if a > 0 and b > 0:
            hypo = (float(a)**2 + float(b)**2)**(0.5)
            return hypo 
        else:
            print 'Error, non-zero numbers required'   
            return False

    elif type(a) not in accept:
        print 'a is not the correct type!'
        return False
    elif type(b) not in accept:
        print 'b is not the correct type!'
        return False  


print pythag(-1,12)
