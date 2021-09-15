# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:19:16 2021

@author: Joseph Thomas
"""
def mul(n):
    sum=0
    
    for i in range(n) :
        if i % 3 == 0 or i % 5 == 0  :
           sum=sum+i
        
    print(sum)
            
                
                
             
mul(1000)
            
    