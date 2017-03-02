
import numpy as np
import GWmodel
import GWplot

model = GWmodel.GWmodel(0,1)
model.setK(1)

for i in range(100):
    if i in range(30,70):
        model.setDirBC(100, i, 0)
  
    else:
        model.setDirBC(0, i, 0)
    
model.solve()

model.out()

plotter = GWplot.GWplot()
#plotter.plot1D(model.out())
plotter.plot1DTr('C:\Users\Jack\Documents\Computational_methods_2017\CompMethodsProject\SolveGWFlow\head.txt')