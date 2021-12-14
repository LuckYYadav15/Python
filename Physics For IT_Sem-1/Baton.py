#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 07:13:32 2021

@author: iiitdwd
"""

""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2012; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2012.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""  

# Baton.py: Combine Ball and Path classes to form Baton
from pylab import *
import numpy
import Ball, Path                                  # import other classes

ion()

class Baton(Ball.Ball, Path.Path):   # Baton inherits Ball and Path props
    def __init__(self, mass, radius, v0, theta, L1, w1): #construct Baton
        Ball.Ball.__init__(self, mass, radius)           # construct Ball
        Path.Path.__init__(self, v0, theta)              # construct Path
        self.L = L1                                        # Baton length
        self.w = w1                                  # Baton ang velocity
        
    def getM(self):
        return 2.0*self.getM1()
        
    def getI(self):
        return (2*self.getI1() + 0.5*self.getM()*self.L**2)
        
    def getXa(self, t):
        xa = self.getX(t) +  0.5*self.L*cos(self.w*t)
        return xa
        
    def getYa(self, t):
        return self.getY(t) +  0.5*self.L*sin(self.w*t)

    def getXb(self, t):
        return self.getX(t) -  0.5*self.L*cos(self.w*t)
        
    def getYb(self, t):
        return self.getY(t) -  0.5*self.L*sin(self.w*t)
        
    def position(self):
      
        t = 0.0                                  # start motion at time 0
        count = 4
        xao = self.getXa(t)                                       # Xa
        yao = self.getYa(t)                                       # Yb
        xbo = self.getXb(t)                                       # Xa
        ybo = self.getYb(t)                                       # Yb
        xco = self.getX(t)                                       # Xa
        yco = self.getY(t)                                       # Yb
        plot([xao,xbo], [yao,ybo],'m')
        t  += 0.02                                   # increment time
        while (self.getYa(t)>= 0.0):                    # do till y Yb <0
            xa = self.getXa(t)                                       # Xa
            ya = self.getYa(t)                                       # Yb
            xb = self.getXb(t)
            yb = self.getYb(t)
            print ya,t,count
            xc = self.getX(t)                                     # Xcom
            yc = self.getY(t)                                     # Ycom
            plot([xao,xa], [yao,ya],'-or')       
            plot([xbo,xb], [ybo,yb],'-ob')       
            plot([xa,xb], [ya,yb],'m')
            plot([xco,xc], [yco,yc],'k')       
            draw()
            xao = xa
            yao = ya
            xbo = xb
            ybo = yb
            xco = xc
            yco = yc

            t  += 0.02                                   # increment time
            count   += 1
         
mybaton = Baton(0.5, 0.4, 15.0, 45.0, 2.5, 22.0)       # m r v0 theta L w
                #next title and geometry for the graph
mybaton.position()                                     # ymax=10, ymin=-1
    
    
        
