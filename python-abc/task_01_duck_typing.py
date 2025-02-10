#!/usr/bin/python3
"""
shape class
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class Shape
    """

    @abstractmethod
    def area(self):
        """
        Abstract method area
        """

        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method perimeter
        """

        pass


class Circle(ABC):
    """
    Circle class
    """

    def __init__(self, radius):
        """
        Initialize Circle class
        """

        self.__radius = abs(radius)

    def area(self):
        """
        area of circle
        """

        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """
        perimeter return
        """

        return 2 * math.pi * self.__radius


class Rectangle(ABC):
    """
    Rectangle class
    """

    def __init__(self, width, height):
        """
        init rectangle
        Arg:
        width (int): width
        height (int): height
        """

        self.__width = width
        self.__heigth = height

    def area(self):
        """
        area rectangle
        """
        return self.__width * self.__heigth

    def perimeter(self):
        """
        Defines the perimeter 
        """
        return 2 * (self.__width + self.__heigth)


def shape_info(shape):
    """
    shape info
    """

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
