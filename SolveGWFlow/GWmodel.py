# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:21:25 2017

@author: Jack
"""
import numpy as np
class GWmodel(object):
 
    def __init__(self, state, dim):
        self.BC = np.zeros((1,3))
        
        if state == 0:
            self.rhs = 0 #steady state condition
        else:
            raise ValueError('Only steady-state conditions are supported in this release' )
            #Demand that changing head with time data be added/calculated
        
        if dim == 1:
            self.dim = 1
        else:
            raise ValueError('Only one dimension is supported in this release' )
            #higher dimention functionallity not implemented
   
   

    def setK(self, K):
       self.K =K
    
                
    def setDirBC(self, h, X, Y):
        if Y <> 0:
            raise ValueError('Only one dimension is supported in this release' )
        if X < 0:
            raise ValueError('Please use positive positions')
        
        self.BC = np.append(self.BC, [[h, X, Y]], axis = 0)
    
      
        # for the sake of moving forwards in development, I will assume the user inputs these boundary conditions in order of increasing x, 
        # and that h=0 at x=0 is not a valid input. Both of these requirments will be cleaned up later
        if (self.BC[0,0] ==0) and (self.BC[0,1] == 0):
          self.BC = np.delete(self.BC, (0), axis =0) #remove the row of zeroes on top. There HAS to be a more elegant way to do this
#        
        
  
    def setNeuBC(self):
        raise NotImplementedError('Neumann BCs not yet implemented')
    def solve(self):    #current version uses LAPACK to solve one dimensional K* d^2h/dx^2=0 using finite differences
        self.Xsteps = 5 #allow users to control this in the future
        self.dx = (self.BC[0,1] -self.bc[1,1] )/ Xsteps
        A 
        #in the future, solution method depending on bc's , dimension of problem.
        # currently only 1d solution with 2 Direchlet conditions considered
        
        
    def out(self):
        return
        #create an output csv, return array of solution depending on dimensions
        