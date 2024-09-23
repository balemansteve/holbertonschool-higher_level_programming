#!/usr/bin/python3
'''Class Square that defines a square'''


class Square:
    '''Class that defines a square'''

    def __init__(self, size=0):
        '''Initialize square with optional size'''
        self.size = size

    @property
    def size(self):
        '''Getter method to retrieve the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method to set the size with validation'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Method to calculate the area of the square'''
        return self.__size * self.__size

    def my_print(self):
        '''Method to print the square with the character #'''
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
