#!/usr/bin/python3
'''Function that write file'''


def write_file(filename="", text=""):
    '''Block 'with' that open file'''
    with open(filename, 'w') as f:
        '''Function 'write' return the number of characters written'''
        return f.write(text)
