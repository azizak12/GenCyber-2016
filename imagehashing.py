# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 09:38:41 2016

@author: student
"""

import hashlib #add hash library


def md5(fname): #md5 hashing doesn't have a lot of collisions
    hash_md5 = hashlib.md5() #prepare to hash
    with open(fname, "rb") as f: #open a file
        for chunk in iter(lambda: f.read(4096), b""): #for each 4096 byte chunk of the file
            hash_md5.update(chunk) #we gun hash dat
        return hash_md5.hexdigest() #return the hash

filename=""
for i in range(1,31):
    filename="the_wall" + str(i) + ".png"
    
    
print(md5("the_wall18.png"))
print(md5("00000000.png"))


