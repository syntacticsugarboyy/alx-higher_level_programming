#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for idx in matrix:
        row = []
        for jdx in idx:
            x = jdx * jdx
            row.append(x)
        new_matrix.append(row)
    return new_matrix
