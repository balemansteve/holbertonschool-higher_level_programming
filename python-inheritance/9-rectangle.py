#!/usr/bin/python3
"""
Module for Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry
    Args:
        BaseGeometry (class): The base class
    """
    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.width, self.height)
