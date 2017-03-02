
##################################################################################################
#   An object designed to plot outputs from GWmodel.py. Plot1D reads in                          #
#   a datafile where the first column has measurments of position and the second column          #
#   has the head value associated with that position. Columns should be seperated with commas.   #
#   Example input:                                                                               #
#   0.00000   ,10.00000                                                                          #
#   2.50000   ,7.50000                                                                           #   
#   5.00000   ,5.00000                                                                           #     
#                                                                                                #   
#   2D plotting capabilities will be added once GWmodel is capable of solving a multidimensional #
#   GW flow equation                                                                             #                   
#                                                                                                #       
#   -Jack Lange, 2/26/17                                                                         #   
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
        datapd = pd.read_csv(dataFile)
        datapd.columns = ['Position [m]', 'head [m]']   
        plt.plot(datapd['Position [m]'], datapd['head [m]'])
        
        #split imported data into 2 arrays, one for position and one for head
        self.data = np.hsplit(self.data,2)
        self.X = self.data[0]
        self.h = self.data[1]

        #plot results      
      # plt.xlabel('Position, m')
     #  plt.ylabel('Head, m')
      # plt.title('One dimensional steady-state solution to GW flow equation')
#       plt.plot(self.X, self.h, 'ro')
        
                  
    def plot1DTr(self, dataFile):
            
        self.data = np.loadtxt(dataFile, delimiter = ',')
           # dx = 
            #dt =      implement method to read both of these fro mfile 
        dx = 1
        position = np.zeros(self.data.shape[1])
        for i in range(self.data.shape[1]):
            position[i] = i*dx
        for i in range(self.data.shape[0]):
            head = self.data[i,:]
            plt.figure(i)
            plt.plot( position, head)
            
    def plot2D(self):
       raise NotImplementedError('2D functionality not yet implemented')