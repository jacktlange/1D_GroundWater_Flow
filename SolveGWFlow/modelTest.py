
import numpy as np
import GWmodel
import GWplot

model = GWmodel.GWmodel(1,1)
model.setK(1)

for i in range(100):
    if i in range(4,6):
        model.setDirBC(20, i, 0)
  
    else:
        model.setDirBC(0, i, 0)
    
model.solve()  #need option for number of timesteps

model.out()

plotter = GWplot.GWplot()
#plotter.plot1D(model.out())
plotter.plot1DTr('C:\Users\Jack\Documents\Computational_methods_2017\CompMethodsProject\SolveGWFlow\head.txt')