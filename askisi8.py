# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:51:04 2018

@author: Bravebirdie
"""

#άσκηση 8 30 random +ve and -ve numbers + (3άδες = 0)

import numpy as np

x=np.random.random_integers(-30,30, size=30)
num=0
print(x)
flag=1
for i,j in zip(range(0,27),range(1,28)):
    num= (x[i]+x[j])
    if -30<=num<=30:
        for k in range(j+1,29,1):
            if x[k]==-num:
                print(x[i],x[j],x[k])
                flag=0
if flag==1:
    print("Δεν υπάρχει συνδυασμός")

