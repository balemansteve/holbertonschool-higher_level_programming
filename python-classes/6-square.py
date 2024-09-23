#!/usr/bin/python3
'''Class Square that defines a square'''


class Square:
    '''Class that defines a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize square with optional size and position'''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''Getter method to retrieve the position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter method to set the position with validation'''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                any(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''Method to calculate the area of the square'''
        return self.__size * self.__size

    def my_print(self):
        '''Method to print the square with the character #'''
        if self.__size == 0:
            print("")
            return
        
        print("\n" * self.__position[1], end="")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
