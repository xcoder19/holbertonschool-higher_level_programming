#!/usr/bin/python3
"""student class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None:
            return self.__dict__

        else:
            dict = {}
            for x in attrs:
                if hasattr(self, x):
                    dict[x] = getattr(self, x)
            return dict

    def reload_from_json(self, json):
        for x in json:
            setattr(self, x, json[x])
