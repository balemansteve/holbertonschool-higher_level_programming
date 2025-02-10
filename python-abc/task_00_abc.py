#!/usr/bin/python3
"""
Task 00: Abstract class
Module to define a class Animal
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Class Animal
    Abstract class that defines a method that must be implemented in subclasses
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that defines a sound of the animals
        """
        pass

class Dog(Animal):
    """
    Class Dog
    Subclass of Animal that implements the speak method
    """

    def sound(self):
        """
        Method that prints the sound a dog makes
        """
        return("Bark")

class Cat(Animal):
    """
    Class Cat
    Subclass of Animal that implements the sound method
    """

    def sound(self):
        """
        Method that prints the sound a cat makes
        """
        return("Meow")
