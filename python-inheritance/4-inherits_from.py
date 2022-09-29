#!/usr/bin/python3
"""func returns if an obj is an instance of a class"""


def inherits_from(obj, a_class):
    """func returns if an obj is an instance of a class"""
    return isinstance(obj, a_class) and type(obj) != a_class
