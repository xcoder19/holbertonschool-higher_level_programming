#!/usr/bin/python3
""" read file func"""


def read_file(filename=""):
    """ read file func"""

    with open(filename) as file:
        print(file.read())
