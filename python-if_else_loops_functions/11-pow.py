#!/usr/bin/python3
def pow(a, b):
    pow = 1
    while(b != 0):
        pow = a * pow
        b = b - 1
    return pow
