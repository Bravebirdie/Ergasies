# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:44:53 2018

@author: Bravebirdie
"""

import numpy as np
import re


textie=open(raw_input("Please enter the name of the file you wish to open (english text only!!): " ),"r")
f=textie.read().lower()
f=re.sub(r'[^\w]*[".",",","?",";","-","_","(",")"]','',f)
word=f.split()

a=(len(word))
trio=np.chararray(a,itemsize=40)

for i in range(0,len(word)-2,1):
    trio[i]=word[i]+" "+ word[i+1]+" "+word[i+2]

first=np.random.randint(0,len(trio)-2,size=1)    
a=trio[first]

print(a+"\n")
text=3
p = word[first+1]+' '+word[first+2]
match = [s for s in trio if p in s]


while text<=200:
    for i, j in enumerate(trio):
        if j == match[1]:
            
    p = word[i+1]+' '+word[i+2]
    match = [s for s in trio if p in s]
    text+=3 
    print(match)
    
    
