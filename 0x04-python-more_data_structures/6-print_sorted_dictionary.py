#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for i, j in sorted(a_dictionary.items()):
        print("{:d}: {:d}".format(i, j))
