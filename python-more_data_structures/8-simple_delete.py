#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    bool = False
    for i in a_dictionary.keys():
        if i == key:
            bool = True
            break
    if bool is True:
        a_dictionary.pop(key)
    return a_dictionary
