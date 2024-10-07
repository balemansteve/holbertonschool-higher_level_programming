#!/usr/bin/python3
'''Function that append file'''


def append_write(filename="", text=""):
    '''Block 'with' that open file'''
    with open(filename, 'a') as f:
        '''Function 'write' return the number of characters written'''
        return f.write(text)
