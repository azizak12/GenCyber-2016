# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 11:54:36 2016

@author: student
"""

def evenodd (given):
    if given != int:
        return
    if given % 2 == 0:
        print("Even")
    else:
        print("Odd")
    
        

def bigsmall (given):
    if given != int:
        return
    if given >= 100:
        print("Big")
    else:
        print("Small")

        
def combo (given):
    if given != int:
        return
    if given % 2 == 0 and given >= 100:
        print("Big/Even")
    elif given % 2 != 0 and given >= 100:
        print("Big/Odd")
    elif given % 2 == 0 and given <= 100:
        print("Small/Even")
    elif given % 2 != 0 and given <= 100:
        print("Small/Odd")

combo(12.2)

