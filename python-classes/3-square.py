#!/usr/bin/python3
'''Class Square that defines a square'''


class Square:
    '''Class with an attribute'''
    def __init__(self, size=0):
        self.__size = size
        '''Size attribute is defined'''
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''Area method is defined'''
        return self.__size * self.__size
    pass
