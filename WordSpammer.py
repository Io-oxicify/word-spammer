#!/usr/bin/python3
from __future__ import print_function  

import time

try:
    input_func = raw_input  
except NameError:
    input_func = input 

print("word spammer by Io")
w = input_func("give me a word or anything to spam: ")
t = input_func("Delay? 0 means no delay. (in seconds)")

try:
    t = (float(t))
except ValueError:
    print("this aint a valid number, defaulting to 0.")
    t = 0
    time.sleep(1)

while True:
    print(w)
    time.sleep(float(t))
