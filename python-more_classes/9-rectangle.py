#!/usr/bin/python3
""""Rectangle class"""


class Rectangle:
    """"Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1
        self.height = height
        self.width = width

    def __del__(self):
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        arr = ''
        if (self.__width == 0 or self.__height == 0):
            return arr
        for x in range(self.__height):
            for i in range(self.__width):
                arr = arr + str(self.print_symbol)
            arr = arr + '\n'
        return arr[:len(arr) - 1]

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (self.__height + self.__width) * 2

    def square(cls, size=0):
        width = height = size
        return cls(width, height)
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
