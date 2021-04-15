"""Peter Rasmussen, Lab 3, variable_value_list.py

This module provides the list VariableValueList class, which is a node in the EvaluationList class.

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
        self.name = ""
        self.valid = True
        self.variables = []
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
            self.echoed_input += symbol
            if symbol not in self.symbols.other_symbols:
                self.name += symbol
        if self.symbols.is_variable(symbol):
            self.variables.append(symbol)

    def display(self) -> None:
        """
        Display construction of linked list.
        Overwrites SinglyLinkedList method of same name.
        :return: None
        """
        print(f"Head: {self.head}")
        temp = self.head
        for i in range(1, self.size + 1):
            print(f"Rank {i}, {temp}, Next: {temp.next_node}")
            temp = temp.next_node

    def get_node(self, variable):
        if variable not in self.variables:
            raise ValueError("Variable not in set of variables.")
        temp = self.head
        for i in range(1, self.size + 1):
            if temp.variable == variable:
                return temp
            temp = temp.next_node
