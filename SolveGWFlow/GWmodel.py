##################################################################################################
#   An object that is capable of solving the GW flow equation. Currently it is                   
#    capable of solving the one dimensional, homogenous, steady-state or transient case.                  
#                                                                                                   
#   Workflow for 1D steady-state solution:                                                       
#       Initialize a GWmodel object                                                              
#       Set Direchlet BC's, in order of increasing position                                      
#       Solve the system                                                                         
#       Output a .csv                                                                            
#       Use GWplot.py to visualize your results                                                   
#   Workflow for 1D transient solution            
#       Initialize a GWmodel object                                                              
#       Use setDirBC to initialize the head value at each point in the domain at time zero   
#       Neuman boundary conditions (dh/dx = 0) are assumed on both boundaries of the domain                              
#       Solve the system                                                                         
#       Output a .csv                                                                            
#       Use GWplot.py to visualize your results                                                                                   
#   -Jack Lange 3/1/2017                                                                          
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
            self.state = 'steady'
        else:
           self.state = 'transient'
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
        if self.state == 'steady':
        # Establish the resolution of the solution
             self.numPoints = self.BC.shape[0] #allow users to choose the resolution of their solution in the future
             self.Xsteps = self.numPoints - 2 #When 2 direchlet BC's are used head must be solved at numPoints-2 locations
             self.dx = (self.BC[1,1] -self.BC[0,1] )/(self.numPoints - 1)  #This and the value of K are useless for solving the steady-state case
             self.dt = 0
             self.K = 0
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
        #in the future, method of solution should depend on the type of boundary conditions and the number dimensions considered

        #Soultion for transient one dimensional GW flow (One dimensional diffusion equation)
                #Boundary conditions required: head at time zero, at all points of interest
        elif self.state == 'transient':
            self.numPoints = self.BC.shape[0]
            self.Xsteps = self.numPoints -1
        
        
        
        
            self.dx = (self.BC[self.numPoints-1,1] -self.BC[0,1] )/(self.Xsteps)
            self.dt =0.5 * self.dx * self.dx * self.K   #condition for convergence
  
        
            self.timeElapsed = 100 * self.dt  #should be a user input 
            self.timeSteps = int( self.timeElapsed / self.dt )
        
        
        
            self.h = np.zeros((self.timeSteps+1, self.numPoints+1) )   #each new row will  be a new timestep, each column will rpresent a position in x
            

            for t in range(0,self.timeSteps+1):
                for x in range(0,self.numPoints):
                
                    if t == 0:
                    #put initial conditions into self.h
                        self.h[t, x] = self.BC[x, 0]
                   
                    elif  x == 0 and t <> 0:
                        self.h[t, x] = (self.dt * self.K / (self.dx * self.dx))*( self.h[t-1, x +1] - 2* self.h[t-1, x] +self.h[t-1, x +1] ) + self.h[t-1, x ]  
                    elif x == self.numPoints and t <> 0:
                        self.h[t, x] = (self.dt * self.K / (self.dx * self.dx))*( self.h[t-1, x ] - 2* self.h[t-1, x] +self.h[t-1, x -1] ) + self.h[t-1, x ]  
                    elif t <> 0: #need if else for edges!
                    #solve for new head at timestep using a forwards difference discretization for the time derrivative
                        self.h[t, x] = (self.dt * self.K / (self.dx * self.dx))*( self.h[t-1, x +1] - 2* self.h[t-1, x] +self.h[t-1, x -1] ) + self.h[t-1, x ]  
                    #at some point, associate a time with each solution in the 
            return self.h
        
        
        
        
        
    #createn output csv for head, outputting the most recent solution. The header contains dx and dt values.
    #returns the location of the output file   
    def out(self):   
      
        HeadOut = 'C:\Users\Jack\Documents\Computational_methods_2017\CompMethodsProject\SolveGWFlow\head.txt'
        np.savetxt(HeadOut, self.h, fmt = '%-10.5f', delimiter = ',', newline = '\n',header='dx,%f,dt,%f,K,%f,' %(self.dx,self.dt, self.K))
        return HeadOut