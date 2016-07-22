# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 10:36:23 2016

@author: student
"""

hex_digit = input("Hex input: ")
bin_digit = bin(int("0x" + hex_digit, 16))
print(bin_digit)
