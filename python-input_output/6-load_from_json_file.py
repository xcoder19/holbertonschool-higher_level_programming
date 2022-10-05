#!/usr/bin/python3
"""load from json"""


import json

def load_from_json_file(filename):
    """load from json"""
    with open(filename) as file:
        json.loads(filename)
