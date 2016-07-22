# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:45:23 2016

@author: student
"""


import random
def randencryptCC(message):
    encrypt_message = ''
    shift = random.randint(1,26)
    for char in message:
        ascii_value = ord(char)
        if ascii_value > 65 and ascii_value < 91:
            if (ascii_value + shift) > 90:
                encrypt_message += chr((ascii_value-26)+ shift)
            else:
                encrypt_message += chr(ascii_value + shift)
        elif ascii_value >97 and ascii_value < 123:
            if (ascii_value + shift) > 122:
                encrypt_message += chr((ascii_value-26) + shift)
            else:
                encrypt_message += chr(ascii_value + shift)
    return encrypt_message



def encryptCC(message,shift):
    encrypt_message = ''
    for char in message:
        ascii_value = ord(char)
        if ascii_value > 65 and ascii_value < 91:
            if (ascii_value + shift) > 90:
                encrypt_message += chr((ascii_value-26)+ shift)
            else:
                encrypt_message += chr(ascii_value + shift)
        elif ascii_value >97 and ascii_value < 123:
            if (ascii_value + shift) > 122:
                encrypt_message += chr((ascii_value-26) + shift)
            else:
                encrypt_message += chr(ascii_value + shift)
    return encrypt_message

print(encryptCC("Hello", 1))

def decryptCC(message):
            for x in range (26):
                decrypt_message = ""
                for char in message:
                    ascii_value = ord(char)
                    if ascii_value >= 65 and ascii_value <= 91:
                        ascii_value -= x
                        if ascii_value < 65:
                            ascii_value += 26
                        decrypt_message += chr(ascii_value)
                    elif ascii_value <=122 and ascii_value >= 97:
                        ascii_value -= x
                        if ascii_value < 97:
                            ascii_value += 26
                        decrypt_message += chr(ascii_value)
                    else:
                        decrypt_message += char
                print(x, decrypt_message)
            return (x)

print(decryptCC("IFMMP"))



        
            

            
