# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:44:21 2017

@author: Jack
"""
import numpy as np
import GWmodel

model = GWmodel.GWmodel(0,1)
model.setDirBC(1, 0, 0)
model.setDirBC(0, 1, 0)


model.solve()
print(model.out())