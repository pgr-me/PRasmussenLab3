"""Peter Rasmussen, Lab 3, polynomial_list.py

This module provides the list evaluation classes EvaluationList and ValuesList. EvaluationList is a
list of ValuesList lists. Both classes inherit from the SinglyLinkedList class.

"""

# Standard library imports
from typing import Union

# Local imports

# Local imports
from lab3.lists.singly_linked_list import SinglyLinkedList


class EvaluationList(SinglyLinkedList):
    """Singly-linked list modified for polynomial evaluation."""

    def __init__(self):
        """Construct an empty list."""
        super().__init__()

        # metrics
        self.line: Union[int, None] = 0

    def set_line(self, line: int):
        """
        Set line number.
        :return:
        """
        self.line = line

    def validate_variables(self):
        """
        Validate that each node has the same set of variables.
        :return:
        """
        pass


class ValuesList(SinglyLinkedList):
    """Singly-linked list modified to validate variable: value pairs."""

    def __init__(self):
        """Construct an empty list."""
        super().__init__()
        self.valid = True

    def validate_nodes(self) -> bool:
        """
        Validate if nodes follow variable-value ... variable-value pattern.
        :return: True if nodes are valid
        """

        return self.valid
