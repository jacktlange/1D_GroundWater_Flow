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



def tridiag(a, b, c, k1=-1, k2=0, k3=1):
    return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)

a = [1, 1]; b = [2, 2, 2]; c = [3, 3]
A = tridiag(a, b, c)
print(A)
