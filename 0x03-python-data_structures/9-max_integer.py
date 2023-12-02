#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None or my_list == []:
        return None

    size = len(my_list)
    i = 0
    max = my_list[i]
    while i < size:
        if max < my_list[i]:
            max = my_list[i]
        i += 1
    return max
