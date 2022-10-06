#!/usr/bin/python3
"""base class"""


class Base:
    """base class"""


    __nb_objects = 0
    def __init__(self, id=None):
        self.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
