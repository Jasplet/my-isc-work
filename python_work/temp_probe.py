#! /usr/bin/python2.7
#
#Script for temp probe.

import serial
import datetime 
import io # input output moduel
from datetime import timedelta
from csv import reader #csv is a module for handling csv files....
ser = serial.Serial(port = '/dev/ttyUSB0',baudrate= 9600,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE)
outfile = '/home/user01/my-isc-work/python_work/serial_temp.tsv'

#print datetime.datetime.utcnow().isoformat(), ser.read(size=8) 

datastring = ser.read(size=8)
date = datetime.datetime.utcnow().isoformat()
start = datetime.datetime.utcnow()
print start 
end = start + timedelta(minutes= 2)
t =  datetime.datetime.utcnow()
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser,1),encoding='ascii',newline='\r')
with open(outfile,'a') as f : #appends to existing file
    f.write('Time\tTemperature (degC)')
    f.flush() 
    while t < end and ser.isOpen():
    
        print 'Time at loop beg is:', t
        try :
            #datastring = ser.read(size=8)
            datastring = sio.readline()
            t = datetime.datetime.utcnow()
            f.write(t.isoformat() + '\t' + datastring + '\n') # writes time and temp measurement to a textfile
            f.flush()
            #print t.isoformat(), datastring
        except KeyboardInterrupt:
            print 'Time to Stop Now'
            ser.close()

ser.close()


def time_conv(t):
    t = datetime.strptime(t, '%Y-%m-%dT%H:%M:%S.%f') # converts time saved in my .tsv file and returns a datetime obejct
    return t

def CtoK(T_C)
    T_K = T_C + 273.15 #Converts temperatures in celsius to Kelvin 
    return T_K

infile = 'serial_temp.tsv'
outfile = 'sensor_data.nc'

#we will need to parse the data to python lists
t = []
temp = []
#Open our tsv file and have a read
with open(infile, 'rb') as tsv:
    tsvreader = reader(tsv,delimeter = '\t')
    for row in tsvreader:
        t.append(time_conv(row[0])) #for each row in the file we read feed to first item (time) into my conversion funciton and append the resutl to the times list
        temp.append(CtoK(row[1])) #for each row we read feed to second item (temp) into my conversion funciton and append the resutl to the temperature list
