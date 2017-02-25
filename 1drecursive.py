# 2/15/17 
# Solution to one dimensional, steady state GW flow equation
#   d^2*h  /dx^2 = 0
#
#2nd order diffeq, linear, need 2 boundary conditions

    
def recursiveSolution(head,i,X,step):
        
    if (i <> 0) and (i <> (points-1)):
        return .5*(recursiveSolution(head,i+1,100,5)-recursiveSolution(head, i-1,100,5))    
    else:
      return head[i]
        

        #return recursiveSolution(head,i+1,100,5)
      
step =5
HeadX1= 500
HeadX2= 250
X=100
points = 20

head =[0 for i in range (points)]

head[0] = HeadX1
head[points-1 ] = HeadX2        


        
#for i in range(1,19):  
    

        
          #  head[i]=.5*(recursiveSolution(head,i+1,100,5)-recursiveSolution(head, i-1,100,5))

#for i in range(20):  #needs to be 1 to 19
   # print head[i] 
        