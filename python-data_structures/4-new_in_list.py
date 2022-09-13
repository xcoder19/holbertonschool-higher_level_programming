#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        new_list=[]
        for x in range(len(my_list)-1):
            if (x == idx):
                new_list[idx] = element
            else:
                new_list[x] = my_list[x]
    return new_list
   
