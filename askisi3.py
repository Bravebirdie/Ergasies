# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 19:04:50 2018

@author: Bravebirdie
"""

#askisi3 rot13 για τους χαρακτήρες του κειμένου

import string as str
from string import ascii_lowercase as lc, ascii_uppercase as uc 
 
def rot13(text):
    text=raw_input('Please insert your text in english, or type exit to stop: ')
    if text=='exit': #γιατί στο current command του Spyder το μεταφράζει και δεν βγαίνει
        k=0
        print('OK BOSS!')
        return k
    else:    
        trans = str.maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13])
        enctext = str.translate(text, trans)
        print(enctext)
    enctext=0
    
    return rot13(text)
 
text='0'
rot13(text)
























