#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub_list in matrix:
        print(" ".join("{:d}".format(number) for number in sub_list))
