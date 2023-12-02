#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    Rows = len(matrix)
    columns = len(matrix[0])
    for i in range(0, Rows):
        for j in range(0, columns):
            if j == columns - 1:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
        print()
