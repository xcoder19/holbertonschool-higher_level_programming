#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for i in set_2:
        bool = False
        for x in set_1:
            if i == x:
                bool = True
        if bool is False:
            new_set.append(i)

    for i in set_1:
        bool = False
        for x in set_2:
            if i == x:
                bool = True
        if bool is False:
            new_set.append(i) 
    return new_set
