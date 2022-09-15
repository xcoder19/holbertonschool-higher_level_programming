#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if len(a_dictionary) == 0:
        return None
    for i in a_dictionary.values():
        if i > max:
            max = i
    return max
