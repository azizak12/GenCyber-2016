# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:22:20 2016

@author: student
"""

lst = [] #this is an empty list: type of one-dimensional (one parameter) database
lst.append("sharifa")
print(lst)
lst.append(64) #append --> things are added from left to right
print(lst)

print(lst[0]) #index

for item in lst:
    print(item) #prints on different lines
    
lst.pop(0) #takes out the corresponding index
print(lst)


lst.remove("Sharifa") #takes out by corresponding value 
print(lst)