#!/usr/bin/python3
"""
A new Class Verboselist
"""


class VerboseList(list):
    """
    A class that inherits from list and adds a verbose mode
    """

    def append(self, item):
        """
        Appends an item to the list and prints a message
        if verbose is True
        """
        super().append(item)
        print(f"Added [{item}] to the list")

    def extend(self, items):
        """
        Extends the list with multiple items and prints a message
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Removes an item from the list and prints a message
        """
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from the list.")
        else:
            print(f"Item [{item}] not found in the list.")

    def pop(self, index=-1):
        """
        Removes an item at a specific index and prints a message
        """
        if len(self) > 0:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
            return item
        else:
            print("The list is empty.")
