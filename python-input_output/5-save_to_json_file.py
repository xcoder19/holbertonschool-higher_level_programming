#!/usr/bin/python3
"""save_to_json_file"""
import json
def save_to_json_file(my_obj, filename):
    """save_to_json_file"""
    text = json.dumps(list(my_obj))
    with open(filename, 'w') as file:
        file.write(text)
