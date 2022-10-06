#!/usr/bin/python3
""" class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area function """
        return self.__width * self.__height

    def display(self):
        """display function"""
        
        if(self.__y > 0):
                print(' ')
        for x in range(self.height):
            if (self.__x > 0):
                print(' ',end="")
            
            for i in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        m = self
        return(
            f"[Rectangle] ({m.id}) {m.x}/{m.y} - {m.width}/{m.height}")
