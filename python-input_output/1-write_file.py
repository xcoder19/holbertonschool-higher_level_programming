#!/usr/bin/python3

""" write file func"""


def write_file(filename="", text=""):
    """ write file func"""
    a = 0
    with open(filename, 'a') as file:
        file.write(text)
        a = a + 1
    return a
