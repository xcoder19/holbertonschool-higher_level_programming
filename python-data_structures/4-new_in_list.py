#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        new_list = []
        index = 0
        for x in my_list:
            if len(my_list) - 1 > index:
                break
            
            elif idx == index:
                new_list[idx] = element
            else:
                new_list[index] = x
            index = index + 1
    return new_list
