#!/usr/bin/python3
from json import JSONEncoder


def to_json_string(my_obj):
    return JSONEncoder.encode(my_obj)