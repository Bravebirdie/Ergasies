# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 18:06:33 2018

@author: Bravebirdie
"""
#άσκηση 8 30 random +ve and -ve numbers + (3άδες = 0)

import numpy as np

x=np.random.random_integers(-30,30, size=30)
print(x)
flag=1
     
y=np.unique(x)

for i in range(0,(len(y)-2),1):
    for j in range(1,(len(y)-1),1):
        num=(y[i]+y[j])
        for k in range(2,len(y),1):
            if y[k]==-num:
                print(y[i],y[j],y[k])
                flag=0

if flag==1:
    print("Δεν υπάρχει συνδυασμός")
