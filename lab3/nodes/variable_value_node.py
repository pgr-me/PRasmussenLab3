"""Peter Rasmussen, Lab 3, variable_value_node.py

This module provides the SimpleNode, Node, and PolynomialNode classes.
The SimpleNode and PolynomialNode classes are the building blocks of the SinglyLinkedList and
DoublyLinkedCircularList classes used for polynomial simplification and evaluation.

"""

# Standard library imports
from time import time_ns
from typing import Union, Dict

# Local imports
from lab3.nodes.simple_node import SimpleNode
from lab3.symbols import Symbols


class VariableValueNode(SimpleNode):
    """
    Node customized for simplifying and organizing polynomial expressions.
    Includes sign and coef attributes which are used for polynomial expression simplification and
    evaluation.
    """

    def __init__(self, name: Union[str, None] = None):
        """
        Set name and optionally set data attributes.
        :param name: PolynomialNode name
        """
        super().__init__(name)
        # function arguments
        # e.g., {"xy": {"coef": 1, "sign" 1}, ...}
        self.sign: Union[int, str] = ""
        self.symbols = Symbols()
        self.valid = True
        self.value: Union[int, str] = ""
        self.variable: Union[None, str] = name
        self.ready_for_processing = False

    def update_node(self, symbol: str):
        """
        Update node data using polynomial term data.
        :param symbol: Symbol to update node with
        :return: None
        """
        self.set_variable(symbol)
        self.set_sign(symbol)
        self.append_numeral(symbol)

    def append_numeral(self, symbol):
        """
        Append numeral to value string.
        :param symbol: Symbol to set if a numeral
        :return:
        """
        # If term is empty, don't update the node with it
        if self.symbols.is_numeral(symbol):
            self.value += symbol

    def set_sign(self, symbol):
        """
        Set sign of node.
        :return: None
        """
        if symbol == "-":
            self.sign = symbol

    def set_variable(self, symbol):
        """
        Assign variable to node.
        :return:
        """
        if self.symbols.is_variable(symbol):
            self.variable = symbol
            self.name = symbol

    def is_symbol_valid(self, symbol) -> bool:
        if not self.symbols.is_accepted_symbol(symbol):
            self.valid = False
        return self.valid

    def is_ready_for_processing(self) -> bool:
        """
        Determine if node is ready for processing.
        :return: True if node is ready for processing
        """
        if self.value != "" and self.name is not None:
            self.ready_for_processing = True

        return self.ready_for_processing

    def process_node(self):
        """
        Convert node value and sign to integers.
        :return: None
        """
        self.is_ready_for_processing()
        if self.ready_for_processing:
            if self.sign == "-":
                self.sign = -1
            else:
                self.sign = 1
            self.value = int(self.value) * self.sign
