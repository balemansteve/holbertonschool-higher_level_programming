#!/usr/bin/python3
"""
Defines the fish class
"""


class Fish:
    """This is the Fish class representing a fish."""

    def swim(self):
        """This method prints a message indicating that the
        fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """This method prints a message describing
        the fish's habitat.
        """
        print("The fish lives in water")


# Define the Bird class
class Bird:
    """This is the Bird class representing a bird."""

    def fly(self):
        """This method prints a message indicating that
        the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """This method prints a message describing the bird's
        habitat.
        """
        print("The bird lives in the sky")


# Define the FlyingFish class
class FlyingFish(Fish, Bird):
    """This is the FlyingFish class representing a flying
    fish. It inherits from both Fish and Bird.
    """

    def swim(self):
        """This method overrides the swim method from Fish to
        print a custom message."""
        print("The flying fish is swimming!")

    def fly(self):
        """This method overrides the fly method from Bird to
        print a custom message."""
        print("The flying fish is soaring!")

    def habitat(self):
        """This method overrides the habitat method from both
        Fish and Bird to print a custom message."""
        print("The flying fish lives both in water and the sky!")
