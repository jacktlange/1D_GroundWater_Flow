

import numpy as np
import GWmodel
import GWplot
from matplotlib import pyplot as plt




#Uncomment below to observe a steady state solution to the 1d GW flow equation

model = GWmodel.GWmodel(0,1)

model.setDirBC(20, 0, 0)
model.setDirBC(0, 20, 0)
   
model.solve(20)  

model.out()

plotter = GWplot.GWplot()

plotter.plot1D(model.out())

plt.show()









#Uncomment below and run to observe a transient case solution

#model = GWmodel.GWmodel(1,1)
#model.setK(1)
#
#for i in range(100):
#    if i in range(4,6):
#        model.setDirBC(20, i, 0)
#  
#    else:
#        model.setDirBC(0, i, 0)
#    
#model.solve(15)  
#
#model.out()
#
#plotter = GWplot.GWplot()
#
#plotter.plot1DTr('C:\Users\Jack\Documents\Computational_methods_2017\CompMethodsProject\SolveGWFlow\head.txt')
