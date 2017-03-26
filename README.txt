

3/2/17
Jack Lange

Current version of the GW model supports solutions of the Homogenous, Isotropic 1D ground water 
flow equation for transient and steady state cases. 


Workflow:

	GWmodel init takes arguments (state, dimension)
	state- string,'steady' or 'transient'
	dimension-int, 1  


	Set boundary conditions using setDirBC(h,X,Y)
	h- float, head value
	X- float, x position
	Y- float, y position

	Once boundary conditions are set, solve using solve(numpoints)
	numpoints- float, controls the number of points in the range of the model

	Use GWplot to display the results. GWplot init takes no arguments

	plot1D(dataFile)
	dataFile- a csv file in the format 
	# dx,1.000000,dt,0.500000,K,1.000000,
	head, head, head, head....
	head, head, head, head...
	.
	.	
	.
	
	Where each column represents a position and each row is a new timestep. Head is a f
	float indicating the head at a position

main.py contains examples of running the model and plotting results for both transient
and steady state cases. 
