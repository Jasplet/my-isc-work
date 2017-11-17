#! /usr/bin/python2.7
#
#Script for temp probe.

import serial
import datetime 
import io # input output moduel
from datetime import timedelta
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
