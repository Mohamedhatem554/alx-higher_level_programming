#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    x = len(my_list) - 1
    for a in my_list:
        print("{}".format(my_list[x]))
        x -= 1
