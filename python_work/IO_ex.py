#! /usr/bin/python
# Exercise on input and output to files

print 'Part One. \nReading a csv file'

with open( './example_data/weather.csv', 'r') as readfile: #using with means we dont have  to worry about closing the file. Readfile is a variable holding the open file pointer
    data = readfile.read() #Actually reads data from the file
    print 'The data from weather.csv has been read. Here it is:'
    print data 

print 'Part Two. \nReading line-by-line'

with open( './example_data/weather.csv', 'r') as readfile:
    data  = readfile.readline().replace("\n","") #  Note how we can stack multiple methods from different objects together !
    print data
    while data != "": # while the variable data is NOT empty
        data = readfile.readline().replace("\n", "")
	#data2 = data.replace("0", "#")
        print data

print "It's over, it's finally over"

print 'Part Three. Reading with a for loop and extracting values'

with open('./example_data/weather.csv','r') as readfile:
    line1 = readfile.readline().replace('\n','')
    r = line1.strip().split(',')[-1]
    rain = [r, ]
    for line in readfile:
        print line 
        r = line.strip().split(',')[-1] # Strip removes leading and trialing whitespaces. Split divides the string into a list based on the delimiter. in this case a comma.
        r = float(r) # makes r a float
        rain.append(r) # appends r to the list rain 

print rain

with open('./example_data/rainfall.txt','w') as writefile:
    for r in rain:
        writefile.write( str(r) + '\n')

print 'Part Four. \n Writing and Reading Binary Data'
# firstly we need to import the module struct!
import struct as st # this allows us to pack/unpack binary data

bin_data = st.pack('bbbb',123,12,45,34)
with open('./example_data/myfirstbinary.dat', 'wb') as wb:
    wb.write(bin_data)

with open('./example_data/myfirstbinary.dat', 'rb') as wr:
    bin_data2 = wr.read()

data = st.unpack('bbbb', bin_data2)
print data


