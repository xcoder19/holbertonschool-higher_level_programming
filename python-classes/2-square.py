#!/usr/bin/python3
"""class square"""


class Square:
    """class square"""
    def __init__(self, size=0):
        if size < 0:
            raise TypeError("size must be >= 0")
        if  not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
