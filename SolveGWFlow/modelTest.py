# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:44:21 2017

@author: Jack
"""
import numpy as np
import GWmodel

model = GWmodel.GWmodel(0,1)
print (model.setDirBC(1, 1, 0))

