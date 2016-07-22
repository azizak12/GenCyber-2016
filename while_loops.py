# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 09:57:49 2016

@author: student
"""

"""
While loop: loop that keeps on running code until
a certain condition is met
"""
"""
import random #library: imports code
"""

"""
myint = 465 #type of counter

while myint > 400:
    #Edit counter
    myint = myint - 5
    #myint -= 5
    print(myint)
"""
"""
guess = int(input("Guess my number "))
number = random.randint(0, 100)


#Number Guessing Game Loop

while guess != number:
    if number < guess:
        print("Aim lower!")
    else:
        print("Aim higher!")
    guess = int(input("Guess again "))
    
print("Congrats, the number is correct!")
print("The number was: ", number)
"""
actualpassword = "FOUR"
guess = input("Guess my password! ")

while guess != actualpassword:
    if guess != actualpassword:
        print("Incorrect. Hint: It's a number 4 characters long")
    guess = input("Guess again ")
print("Correct!")

