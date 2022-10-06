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
