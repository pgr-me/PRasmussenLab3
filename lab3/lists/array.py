"""Peter Rasmussen, Lab 3, lists/array.py

This module provides a simple Array class which the parse_evaluation_input uses to store variable-
value lists.

"""

# Local imports
from lab3.utils import Timer


class Array:
    """Simple array."""

    def __init__(self, size=100):
        """Initialize an empty array"""
        super().__init__()
        self.size = size
        self.array = size * [None]
        self.index = 0

    def append_item(self, item):
        """
        Append an item to the list.
        :param item: Data element to add
        :return: None
        """
        self.array[self.index] = item
        self.index += 1

    def get_item(self, index):
        """
        Get item at given array index.
        :param index: Array index from which to retrieve item
        :return: Item at index
        """
        return self.array[index]

    def pop_item(self):
        """
        Remove item at end of array.
        :return: Popped item
        """
        item = self.array[self.index]
        self.array[self.index] = None
        return item
