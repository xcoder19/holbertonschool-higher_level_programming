#!/usr/bin/python3
def element_at(my_list,idx):
    print(len(my_list))
    if (len(my_list) < idx) or (idx < 0):
        return
    else:
        return my_list[idx]


element_at([1,3,4,5],4)