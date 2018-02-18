# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:32:31 2018

@author: Bravebirdie
"""


#άσκηση 4_λατινικοί αριθμοί
def Romans(num):
    
    
    conv = [[1000000, u'M\u0305 '],[900000,u'C\u0305 M\u0305 '],[500000,u'D\u0305 '],[400000,u'C\u0305 D\u0305 '],
            [100000 , u'C\u0305 '],[90000 ,u'X\u0305 C\u0305 '],[50000, u'L\u0305 '],[40000, u'X\u0305 L\u0305 '],
            [10000  , u'X\u0305 '],[9000  ,u'MX\u0305 '],       [5000,u'V\u0305 '],  [4000, u'MV\u0305 '],
            [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
            [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
            [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
            [   1, 'I']]
    roman = ''

    if num == 0 :
        print('0 in Latin is just Nulla.')
        return
        
    else:    
    
        i = 0 #initiate i = 0
        while num > 0:
            while conv[i][0] > num: 
                i+=1                
            roman += conv[i][1]
            num -= conv[i][0]
            
    print(roman)
    return 

num = int(input("Enter a number between 0 and 1 million or type any negative number to exit: "))
while 0<=num<1000001:
    Romans(num)
    more=raw_input("Do you want to do more conversions to latin? Y/N ")
    if more=='Y':
        num = int(input("Enter a number between 0 and 1 million or type any negative number to exit: "))
    else:
        num=-1



