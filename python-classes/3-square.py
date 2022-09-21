#!/usr/bin/python3
"""class square"""


from ctypes import sizeof


class Square:
    """class square"""
    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size*self.__size
