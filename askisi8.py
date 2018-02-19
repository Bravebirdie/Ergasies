# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 18:06:33 2018

@author: Bravebirdie
"""
#άσκηση 8 30 random +ve and -ve numbers + (3άδες = 0)

import numpy as np

x=np.random.random_integers(-30,30, size=30)

print("Here's a list with 30 random integers in the span (-30,30): ")
print(x)
flag=1
comb=np.zeros((200,3))
c=0
x=np.sort(x)

for i in range(0,(len(x)-2),1):
    for j in range(i,(len(x)-1),1):
        for k in range(j,len(x),1):
            if (x[i]+x[j]+x[k]==0) and (x[i]<=x[j]<x[k]):
                comb[c,:]=np.hstack(([x[i],x[j],x[k]]))
                c+=1
                flag=0

print("Combos found: ")

for i in range(0,c+1,1):
    if comb[i+1,1]<>comb[i,1]:       
        print(comb[i,:])


if flag==1:
    print("No combo available")

