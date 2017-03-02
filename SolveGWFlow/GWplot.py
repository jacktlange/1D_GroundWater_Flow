
##################################################################################################
#   An object designed to plot outputs from GWmodel.py. 
#   plot1D :                      
#   read in a datafile where the first column is calculated head values from GWmodel.py. The header for 
#   the file should include the spacing between each point, time step spacing, and a value of 
#   hydraulic conductivity in the format demonstrated in the example below.
#   EX:                                       
#   # dx,0.010204,dt,0.000000,K,0.000000,  
#   10.00000                                                                         
#   7.50000                                                                              
#   5.00000            
#   
#   Outputs a plot of h vs position 
                                                                  
#                                                                                             
#    plot1dTr :                                                                  
#    read in a datafile where each row is one timestep, and each column represents a position. The 
#     header should follow the same format as plot1D.
 #    EX:
#     # dx,1.000000,dt,0.500000,K,1.000000,         
#     0.00000   ,0.00000   ,0.00000   ,20.00000  ,20.00000  ,0.00000   ,0.00000   ,0.00000   ,0.00000   ,0.00000   
#     0.00000   ,0.00000   ,10.00000  ,10.00000  ,10.00000  ,10.00000  ,0.00000   ,0.00000   ,0.00000   ,0.00000   
#     0.00000   ,5.00000   ,5.00000   ,10.00000  ,10.00000  ,5.00000   ,5.00000   ,0.00000   ,0.00000   ,0.00000   
#     5.00000   ,2.50000   ,7.50000   ,7.50000   ,7.50000   ,7.50000   ,2.50000   ,2.50000   ,0.00000   ,0.00000   
#     2.50000   ,6.25000   ,5.00000   ,7.50000   ,7.50000   ,5.00000   ,5.00000   ,1.25000   ,1.25000   ,0.00000   
#     6.25000   ,3.75000   ,6.87500   ,6.25000   ,6.25000   ,6.25000   ,3.12500   ,3.12500   ,0.62500   ,0.00000   
#     3.75000   ,6.56250   ,5.00000   ,6.56250   ,6.25000   ,4.68750   ,4.68750   ,1.87500   ,1.56250   ,0.00000   
#     6.56250   ,4.37500   ,6.56250   ,5.62500   ,5.62500   ,5.46875   ,3.28125   ,3.12500   ,0.93750   ,0.00000   
#     4.37500   ,6.56250   ,5.00000   ,6.09375   ,5.54688   ,4.45312   ,4.29688   ,2.10938   ,1.56250   ,0.00000   
#     6.56250   ,4.68750   ,6.32812   ,5.27344   ,5.27344   ,4.92188   ,3.28125   ,2.92969   ,1.05469   ,0.00000   
#     4.68750   ,6.44531   ,4.98047   ,5.80078   ,5.09766   ,4.27734   ,3.92578   ,2.16797   ,1.46484   ,0.00000  
#   
#    outputs  a plot of h vs position for each timestep




#   -Jack Lange, 2/26/17 
##################################################################################################

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



class GWplot(object):
    
    def __init__(self):
        return
      
    def plot1D(self, dataFile):
        #load an output file from GWmodel.py
        self.data = np.loadtxt(dataFile, delimiter = ',') 
        #extract information in the header
        txtData = open(dataFile, "r")    
        header = txtData.readline()
        headerSplit = header.split(',')
        dx = float(headerSplit[1])
        dt = float(headerSplit[3])
        K = float(headerSplit[5])
       
        #create a matrix for each position to be plotted
        position = np.zeros(self.data.shape[0])
        for i in range(self.data.shape[0]):
            position[i] = i*dx
        
      

    
        #plot results      
        plt.xlabel('Position, m')
        plt.ylabel('Head, m')
        plt.title('One dimensional steady-state solution to GW flow equation')
        plt.plot(position, self.data, 'ro')
        
                  
    def plot1DTr(self, dataFile):
        #load an output file from GWmodel.py    
        self.data = np.loadtxt(dataFile, delimiter = ',')
        
        #extract information in the header
        txtData = open(dataFile, "r")    
        header = txtData.readline()
        headerSplit = header.split(',')
        dx = float(headerSplit[1])
        dt = float(headerSplit[3])
        K = float(headerSplit[5])
        
        #create a matrix for each position to be plotted
        position = np.zeros(self.data.shape[1])
        for i in range(self.data.shape[1]):
            position[i] = i*dx
        
        #create a figure for each timestep
        for i in range(self.data.shape[0]):
            head = self.data[i,:]
            plt.figure(i)
   
            plt.xlabel('Position, m')
            plt.ylabel('Head, m')
            plt.title('One dimensional transient solution to GW flow equation at timestep: %d' %i)
            plt.plot( position, head)
            
    def plot2D(self):
       raise NotImplementedError('2D functionality not yet implemented')