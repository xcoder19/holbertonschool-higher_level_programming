#!/usr/bin/python3
def multiple_returns(sentence):
    first_character = 'a'
    length = len(sentence)
    if length == 0:
        first_character = None
    tuple = (length,first_character)
    return tuple
