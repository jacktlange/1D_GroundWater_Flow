# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:21:25 2017

@author: Jack
"""

class GWmodel:
    
    def __init__(self, state, dim):
        if state == 0:
            self.rhs =0 #steady state condition
        else:
            raise ValueError('Only steady-state conditions are supported in this release' )
            #Demand that changing head with time data be added/calculated
        if dim == 1:
            self.dim = 1
        else:
            raise ValueError('Only one dimension is supported in this release' )
            #higher dimention functionallity not implemented
    def imData():
        return
        #Check to see if 1 d or 2d
    def setK(K):
        self.K =K
    
        
        #ensure that enough bc's are set
    def setBC(head, value, position):
        return
    def solve():
        return
        #solution method depending on bc's , dimension
    def out():
        return
        #create an output csv, return array of solution depending on dimensions
        