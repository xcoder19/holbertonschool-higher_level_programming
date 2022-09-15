#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    key = ""
    if len(a_dictionary) is None:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] > max:
            max = a_dictionary[i]
            key = i
    return key
