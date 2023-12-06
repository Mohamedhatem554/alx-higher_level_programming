#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    res = []
    for i in matrix:
        sub_matrix = map(lambda sqr: sqr**2, i)
        res.append(list(sub_matrix))
    return res
