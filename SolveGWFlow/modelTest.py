# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:44:21 2017

@author: Jack
"""
import numpy as np
import GWmodel
import GWplot

model = GWmodel.GWmodel(0,1)
model.setDirBC(10, 0, 0)
model.setDirBC(0, 10, 0)


model.solve()


plotter = GWplot.GWplot()
plotter.plot1D(model.out())