#!/usr/bin/python3
def print_reversed_list_interger(my_list=[]):
    if my_list == None:
        return None
    for x in reversed(range(len(my_list))):
        print("{:d}".format(my_list[x]))
