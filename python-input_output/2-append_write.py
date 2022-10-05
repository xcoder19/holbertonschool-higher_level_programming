#!/usr/bin/python3


""" append file func"""


def append_write(filename="", text=""):
    """ append file func"""

    with open(filename, 'a') as file:
        return file.write(text)
