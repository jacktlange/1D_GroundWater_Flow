

import numpy as np
import GWmodel
import GWplot

# steady state solution to the 1d GW flow equation
#
#model = GWmodel.GWmodel('steady',1)
#
#model.setDirBC(20, 0, 0)
#model.setDirBC(0, 20, 0)
#    
#model.solve(20)  
#
#model.out()
#
#plotter = GWplot.GWplot()
#
#plotter.plot1D(model.out())
#
#
#transient case solution

model = GWmodel.GWmodel('transient',1)
model.setK(1)

for i in range(100):
    if i in range(4,6):
        model.setDirBC(20, i, 0)
  
    else:
        model.setDirBC(0, i, 0)
    
model.solve(100)  

model.out()

plotter = GWplot.GWplot()

plotter.plot1DTr('C:\Users\Jack\Documents\Computational_methods_2017\CompMethodsProject\SolveGWFlow\head.txt')
