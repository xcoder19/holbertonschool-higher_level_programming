#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res=[]
    for i in range(len(tuple_a)):
        res.append(tuple_a[i]+tuple_b[i])
    res = tuple(res)
    return res
