
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 06:43:14 2021

@author: iiitdwd
"""

import numpy
import matplotlib.pyplot as plt
from pylab import *
from tools import derive
from tools import derivs
from tools import euler
from tools import rk2
from tools import rk4
N=5000 # Number of iterations
y=numpy.zeros([N])# initialization of memory to save results
y[0]=1 # initial position of the object
tau=50 # total iterative/computation time
dt=tau/float(N-1)# time step for each iteration
time=numpy.linspace(0,tau,N)# creation of time grid for plotting

plt.figure()#starting plot figure
for j in range(N-1):#starting a for loop of iterations
    y[j+1]=rk2(y[j],time[j],dt,derive) # calling euler function for initial state y[j,:], note colon is ignored
plt.plot(time,y,'.r') # plotting position with red line
plt.plot(time,exp(time),'-b')# plotting position with blue line
plt.legend(['iteraive','actual'])
#xlim(45,50)
plt.show()
#plt.draw()
