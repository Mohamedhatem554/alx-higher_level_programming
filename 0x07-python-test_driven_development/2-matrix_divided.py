#!/usr/bin/python3

def matrix_divided(matrix, div):
    Errormsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(Errormsg)
    if not matrix:
        raise TypeError(Errormsg)
    for lists in matrix:
        if not isinstance(lists, list):
            raise TypeError(Errormsg)
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(Errormsg)
    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(Errormsg)
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in lists] for lists in matrix]
