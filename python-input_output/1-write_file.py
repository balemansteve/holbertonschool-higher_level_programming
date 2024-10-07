#!/usr/bin/python3
'''Function that write file'''


def write_file(filename="", text=""):
    '''Block 'with' that open file'''
    with open(filename, 'w') as f:
        '''Function 'write' return an integer representing the number of characters'''
        return f.write(text)
