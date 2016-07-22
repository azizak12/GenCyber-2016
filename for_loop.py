# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 10:41:48 2016

@author: student
"""
"""
#For loop: Stops as long as it's in a certain range

for i in range(0,10,3): #i is a variable that exists inside for loop. Third number shows every third number.
    print(i)

string = "Do you want to be my lover"

for char in string: #goes through each character in the string
    print(char)
    
def ascii_to_eight_bit(letter):
    num = ord(letter)
    bitstring = ""
    for i in range(8):
        print(num)
        if num % 2 == 0:
            bitstring = '0'+ bitstring
            print('0')
        else: 
            bitstring = '1' + bitstring
            print('1')
        num = num // 2
    return bitstring
print(ascii_to_eight_bit('S'))
"""

def goodpassword(password):
    hasUpper = False
    hasLower = False
    if len(password) >= 6:
        for char in password:
            if ord(char) >= 65 and ord(char) <= 98:
                hasUpper = True
            elif ord(char) >= 97 and ord(char) <= 122:
                hasLower = True
        if hasUpper == True and hasLower == True:
            return True
    else:
        return False
print(goodpassword("Loahs72k"))
print(goodpassword("lajs"))


    
            
    