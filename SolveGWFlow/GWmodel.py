##################################################################################################
#   An object that is capable of solving the GW flow equation. Currently it is                   #
#   only capable of solving the one dimensional, homogenous, steady-state case.                  #
#                                                                                                #   
#   Workflow for 1D steady-state solution:                                                       #
#       Initialize a GWmodel object                                                              #
#       Set Direchlet BC's, in order of increasing position                                      #
#       Solve the system                                                                         #
#       Output a .csv                                                                            #
#       Use GWplot.py to visualize your results                                                  # 
#                                                                                                #
#   -Jack Lange 2/26/17                                                                          # 
##################################################################################################


#Initializes a tridiagonal matrix, courtesy of user aamir23 on stackoverflow
# x,y,and z are the values that apear on the diagonal. k(1-3) controls which diagonals x,y, and z appear on
def tridiag(T,x,y,z,k1=-1, k2=0, k3=1):  
    a = [x]*(T-abs(k1)); b = [y]*(T-abs(k2)); c = [z]*(T-abs(k3))
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)





import numpy as np
class GWmodel(object):
 
    #state = 0 corresponds to steady-state
    #dim controls how many dimensions will be considered, currently only 1d is supported
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
   
   
    #Set hydraulic conductivity, unnecessary for the homogenous steady-state case. 
    def setK(self, K):  
       self.K =K
    
      #Set Direchlet boundary conditions.          
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
        
      #set Neumann BC's
    def setNeuBC(self):
        raise NotImplementedError('Neumann BCs not yet implemented')
        
        
    #Set up and solve a system of finite difference equations using LAPACK 
    def solve(self):    #current version is only capable of solving  K* d^2h/dx^2 = 0 
        #Establish the resolution of the solution
        self.numPoints = 5 #allow users to choose the resolution of their solution in the future
        self.Xsteps = self.numPoints - 2 #When 2 direchlet BC's are used head must be solved at numPoints-2 locations
        self.dx = (self.BC[1,1] -self.BC[0,1] )/(self.numPoints - 1)  #This and the value of K are useless for solving the steady-state case
        
        #set up the system of equations, Ah=b
        A = tridiag(self.Xsteps,-1,2,-1)
        b = np.zeros(self.Xsteps)    #zeros only valid for steady state conditions
        #palce boundary conditions in the system
        b[0] = self.BC[0,0]    
        b[self.Xsteps-1] = self.BC[1,0] 
           
        #Solve the system!  (Instert sounds of gears crunching)
        self.h = np.linalg.solve(A,b) 
       
        #append Direchlet BC's to both ends of the list
        self.h = np.append(self.h, self.BC[1,0])
        self.h = np.insert(self.h, 0, self.BC[0,0])
        
        return self.h
        #in the future, method of solution should depend on the type of boundary conditions and the number dimensionsbeing considered

        
    #create an output csv for head, outputting the most recent solution. The first column is position, second is head
    #returns location of the output file   
    def out(self):
       
        #Establish an array that contains each position where head was calculated
        X= np.empty(self.numPoints)
        for i in range(self.numPoints):
            X[i] = i * self.dx
       
        # Connect the position and Head arrays aand print the combination to a text file
        self.hOut = np.stack((X, self.h))
        self.hOut = np.transpose(self.hOut)
        HeadOut = 'C:\Users\Jack\Documents\Computational_methods_2017\CompMethodsProject\SolveGWFlow\head.txt'
        np.savetxt(HeadOut, self.hOut, fmt = '%-10.5f', delimiter = ',', newline = '\n')
       
        return HeadOut