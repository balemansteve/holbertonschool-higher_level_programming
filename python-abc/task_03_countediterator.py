#!/usr/bin/python3
"""
Class that extends the built-in iterator
"""


class CountedIterator:
    """
    Class that extends the built-in iterator
    """

    def __init__(self, iterable):
        """
        Initialize the iterator
        Args:
            iterable: The iterable to iterate over
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def __next__(self):
        """
        Get the next item from the iterator
        Returns:
        The next item from the iterator
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise

    def get_count(self):
        """
        Get the count of items iterated over
        Returns:
        The count of items iterated over
        """
        return self.counter
