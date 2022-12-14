#!/usr/bin/python3
"""base class"""

import json


class Base:
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        """save_to_file"""

        list = []
        with open(f"{cls.__name__}.json", 'w') as file:
            if list_objs is None:
                return json.dumps(list, file)
            else:
                for x in list_objs:
                    list.append(x.to_dictionary())
                file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """"create function"""

        if cls.__name__ == 'Rectangle':
            obj = cls(1, 2)
        else:
            obj = cls(2)
        obj.update(**dictionary)
        return (obj)

    @classmethod
    def load_from_file(cls):
        """load_from_file"""
        listi = []
        try:
            with open(f"{cls.__name__}.json", "r") as file:
                list = cls.from_json_string(file.read())
                for x in list:
                    listi.append(cls.create(x))
                return listi
        except FileNotFoundError:
            return []
