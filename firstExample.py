# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys

counter =0 

while counter < 50:
    counter +=1
    
if counter ==50:
    print ("50")
else:
    print ("error")
    
for i in range(3):
    counter *=10

if counter == 50 * 10  **3:
    print ("checks out -- done ")
    print ("final counter =", counter)
else:
    sys.exit("fail ")
    
print ("now lets divide the counter by 25001 just over half")
print (counter/25001)
print ("now lets divide the counter by 25001 just over half")
print (counter/25001.)