#!/usr/bin/python3
def pow(a, b):
    x = b
    if b < 0:
        x = -b
    pow = 1
    while(x != 0):
        pow = a * pow
        x = x - 1
    if (b < 0):
        return 1 / pow 
    return pow
