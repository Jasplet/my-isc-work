#! /usr/bin/python2.7
import numpy as np 
import matplotlib.pyplot as plt

print 'Part One.\n"My first Plot"'

a = range(10)
plt.plot(a) #creates plot objects
#plt.show(a) # actually shows the plot 

print 'Part Two.\nMultiple Axes Pltos (second exercise)'

fig, ax1 = plt.subplots() #creates our figure and axes variables
time = [0,1,2,3,4,5,6]
Co2 = [250,265,272,260,300,320,289]
temp = [14.1,15.5,16.3,18.1,17.3,19.1,20.2]

ax1.plot(time,Co2,'b--') #Plotting is also a method for axes.,time,temp,'r*-')
ax1.set_ylabel('[Co2]')
ax2 = ax1.twinx()
ax2.set_ylabel('Temp [^o C]')
ax2.plot(time, temp, 'r*-')
plt.title('[Co2] and temp over time')
plt.xlabel('Time (decade)')
plt.show(2)

## Plotting 3 graphs on one page
import numpy as np
import math 
#plt.subplot(1,3,1)

#r = np.arange(0,2,0.01 # r for sprial plot
#theta = 2*np.pi * r # theta for spiral
theta = np.arange(0,2*np.pi,(np.pi/50))
r = 2 -  np.cos(9*theta)
ax = plt.subplot(111,projection='polar')
ax.plot(theta,r)
plt.show()
#plt.subplot(1,3,2)
#y = range(10,0,-1)
#plt.plot(y)
#plt.subplot(1,3,3)
#z = [4] * 10
#plt.plot(z)

plt.show()
### USEFUL FOR PLOTTING. Easy way to make lists with a small interval (eg 0 to 1 in intevals of 0.005)

x = [i/1000. for i in range(0,3601,5)]
print x
plt.figure(3)
import math
sx = [math.sin(i) for i in x]
#plt.plot(x,sx)
#plt.show(3)
