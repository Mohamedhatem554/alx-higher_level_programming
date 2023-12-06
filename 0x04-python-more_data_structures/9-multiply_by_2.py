#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    tmp = a_dictionary.copy()
    for i, k in tmp.items():
        tmp[i] = k * 2
    return tmp
