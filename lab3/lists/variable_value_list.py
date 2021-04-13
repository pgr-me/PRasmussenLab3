"""Peter Rasmussen, Lab 3, variable_value_list.py

This module provides the list evaluation classes EvaluationList and VariableValueList. EvaluationList is a
list of VariableValueList lists. Both classes inherit from the SinglyLinkedList class.

"""

# Standard library imports
from typing import Union

# Local imports

# Local imports
from lab3.lists.singly_linked_list import SinglyLinkedList
from lab3.symbols import Symbols


class VariableValueList(SinglyLinkedList):
    """Singly-linked list modified to validate variable: value pairs."""

    def __init__(self):
        """Construct an empty list."""
        super().__init__()
        self.valid = True
        self.variables = set()
        self.symbols = Symbols()

        # metrics
        self.echoed_input = ""

    def validate_nodes(self) -> bool:
        """
        Validate if nodes follow variable-value ... variable-value pattern.
        :return: True if nodes are valid
        """

        return self.valid

    def record_input(self, symbol):
        """
        Record input symbol.
        :param symbol: Symbol to echo
        :return: None
        """
        if symbol != "\n":
            self.echoed_input = symbol
