#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [[i, replace][i is search] for i in my_list]
