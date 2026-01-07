from __future__ import print_function  
try:
    input_func = raw_input  
except NameError:
    input_func = input 

print("word spammer by Io")
word = input_func("give me a word or anything to spam: ")
while True:
    print(word)