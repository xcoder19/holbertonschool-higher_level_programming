#!/usr/bin/pyton3

def uniq_add(my_list=[]):
    added_int = []
    Result = 0
    for i in my_list:
        exists = False
        for x in added_int:
            if i == x:
                exists = True
        if exists == False:
            added_int.append(i)
            Result = Result + i
    return Result
