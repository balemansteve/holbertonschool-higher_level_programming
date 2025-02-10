#!/usr/bin/python3
"""
Module for Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    Args:
        Rectangle (class): The base class
    """
    def __init__(self, size):
        """
        Initialize a new Square instance
        Args:
            size (int): The size of the square
        """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """
        Return the area of the square
        """
        return self.__size ** 2
