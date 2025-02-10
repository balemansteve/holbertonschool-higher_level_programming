#!/usr/bin/python3
"""
Module for BaseGeometry class
"""


class BaseGeometry:
    """
    Empty class
    """

    def area(self):
        """
        Public instance method to calculate the area of the geometry
        Raises:
            Exception: If the method has not been implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value
        Args:
            name (str): The name
            value (int): The value
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less or equal to 0
        """
        if type(value) is not int:
            raise ValueError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
        else:
            return True
