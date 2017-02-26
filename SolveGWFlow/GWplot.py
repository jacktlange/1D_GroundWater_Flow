# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:09:02 2017

@author: Jack
"""
import matplotlib.pyplot as plt
import numpy as np


class GWplot(object):
    def __init__(self):
        return
        #read in dataset, determine what dimensions, call appropriate method
    def plot1D(self, dataFile):
        self.data = np.loadtxt(dataFile, delimiter = ',')
        self.data = np.transpose(self.data)
        self.data = np.vsplit(self.data,2)
        self.X = self.data[0]
        self.Y = self.data[1]
        plt.plot(self.X, self.Y, 'ro')
                  
        
        
    def plot2D(self):
        return