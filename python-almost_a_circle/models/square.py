#!/usr/bin/python3

"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    def update(self, *args, **kwargs):
        """update function"""
        i = 0
        att = ["id", "size", "x", "y"]
        if (args):
            for x in args:
                if (i < len(att)):
                    setattr(self, att[i], x)
                    i += 1
        else:
            for x in kwargs:
                setattr(self, x, kwargs[x])
 
    def to_dictionary(self):
        """ to_dictionary func"""

        return {'id': self.id, 'size':self.size, 'x': self.x, 'y': self.y}
