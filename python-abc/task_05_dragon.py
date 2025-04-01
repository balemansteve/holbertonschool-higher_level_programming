#!/usr/bin/python3
"""
Defines a Dragon class
"""


# Define the SwimMixin
class SwimMixin:
    """This mixin adds a swimming behavior."""

    def swim(self):
        """Print a message about swimming."""
        print("The creature swims!")


# Define the FlyMixin
class FlyMixin:
    """This mixin adds a flying behavior."""

    def fly(self):
        """Print a message about flying."""
        print("The creature flies!")


# Define the Dragon class
class Dragon(SwimMixin, FlyMixin):
    """The Dragon class can both swim and fly."""

    def roar(self):
        """Print a message about the dragon roaring."""
        print("The dragon roars!")
