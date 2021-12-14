#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 07:15:19 2021

@author: iiitdwd
"""

""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2012; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2012.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp""" 

# Ball.py: Isolated ball with Mass and Radius for OOP

class Ball:
    def __init__(self, mass, radius):            # ball class constructor
        self.m = mass                                   # initialize mass
        self.r = radius                               # initialize radius
        
    def getM1(self):                                      # get ball mass
        return self.m                  
         
    def getR(self):                                          # get radius
        return self.r                             # get moment of inertia
        
    def getI1(self):
        return (2.0/5.0)*self.m*(self.r)**2