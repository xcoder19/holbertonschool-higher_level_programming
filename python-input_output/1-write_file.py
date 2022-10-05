#!/usr/bin/python3

""" write file func"""


def write_file(filename="", text=""):
    """ write file func"""

    with open(filename) as file:
        file.write(text)
