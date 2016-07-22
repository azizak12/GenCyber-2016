# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 15:13:46 2016

@author: student
"""

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
x1 = int(input("Enter value for x1: "))
x2 = int(input("Enter value for x2: "))
x3 = int(input("Enter value for x3: "))
print(a,"^",x1,"+",b,"^",x2,"+",c,"^",x3)
answer = a ** x1 + b ** x2 + c ** x3
print(answer)

