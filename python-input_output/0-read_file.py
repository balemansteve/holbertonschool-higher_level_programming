#!/usr/bin/python3
'''Function that reads file'''


def read_file(filename=""):
    '''Block with that open file'''
    with open(filename, 'r') as f:
        file = f.read()
        print(file, end="")
