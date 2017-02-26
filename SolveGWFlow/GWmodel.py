# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:21:25 2017

@author: Jack
"""


def tridiag(T,x,y,z,k1=-1, k2=0, k3=1):  #Courtesy of user aamir23 on stackoverflow
    a = [x]*(T-abs(k1)); b = [y]*(T-abs(k2)); c = [z]*(T-abs(k3))
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)





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
   
   

    def setK(self, K):  #unnecessary for the steady state case
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
        self.numPoints = 5 #allow users to choose the resolution of their solution in the future
        self.Xsteps = self.numPoints - 2 #When 2 direchlet BC's are used head must be solved at numPoints-2 locations
        self.dx = (self.BC[1,1] -self.BC[0,1] )/(self.numPoints - 1)  #This and the value of K are useless for solving the steady-state case
        A = tridiag(self.Xsteps,-1,2,-1)
        b = np.zeros(self.Xsteps)    #zeros only valid for steady state conditions
        b[0] = self.BC[0,0]    #Place boundary conditions in system
        b[self.Xsteps-1] = self.BC[1,0] 
        self.h = np.linalg.solve(A,b) 
        #append Direchlet BC's to either end of the list
        self.h = np.append(self.h, self.BC[1,0])
        self.h = np.insert(self.h, 0, self.BC[0,0])
        return self.h
        #in the future, method of solution should depend on the type of boundary conditions and 
        # how many dimensions are being considered
        # currently only capable of 1d steady-state solution with 2 Direchlet conditions 
        
        
    def out(self):
        
        #create an output csv for head, outputting the most recent solution. The first column is position, second is head
        #returns location of the output file
        X= np.empty(self.numPoints)
        for i in range(self.numPoints):
            X[i] = i * self.dx
        self.hOut = np.stack((X, self.h))
        self.hOut = np.transpose(self.hOut)
        HeadOut = 'C:\Users\Jack\Documents\Computational_methods_2017\CompMethodsProject\SolveGWFlow\head.txt'
        np.savetxt(HeadOut, self.hOut, fmt = '%-10.5f', delimiter = ',', newline = '\n')
        return HeadOut