#!/usr/bin/python3
def element_at(my_list,idx):
    if (idx < 0) or (len(my_list) < idx):
        return None
    else:
        print("{:d}".format(my_list[idx]))
