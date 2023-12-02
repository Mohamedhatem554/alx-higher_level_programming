#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        pass
    Row = len(matrix)
    Column = len(matrix[i])

    for row in range(Row):
        for column in range(Column):
            print("{:d}".format(matrix[row][column]), end=" ")
        print()
