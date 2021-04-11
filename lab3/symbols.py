"""Peter Rasmussen, Lab 3, symbols.py

This module provides the Symbols class, which bundles variables, operators, and other accepted
symbols into itself.

"""

# standard library imports
from typing import Union


class Symbols:
    """
    This class bundles symbols used for syntax error checking and polynomial expression simplification and evaluation.
    """

    def __init__(
            self, use_numerals: bool = False, additional_operators: Union[None, str] = None
    ):
        self.numerals = "0123456789"
        self.node_names = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.operators = "+-"
        self.variables = "abcdefghijklmnopqrstuvwxyz"
        self.other_symbols = " \t\n"
        self.accepted_symbols = self.node_names + self.numerals + self.operators + self.variables

