"""Peter Rasmussen, Lab 3, symbols.py

This module provides the allowable numerals, node_names, operators, variables, and other symbols
used to organize, simplify, and evaluate polynomial expressions.

"""


class Symbols:
    """
    Bundle of symbols used for syntax error checking and polynomial expression simplification and evaluation.
    """

    def __init__(self):
        self.numerals = "0123456789"
        self.node_names = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.operators = "+-"
        self.variables = "abcdefghijklmnopqrstuvwxyz"
        self.other_symbols = "\t\n "
        self.accepted_symbols = self.node_names + self.numerals + self.operators + self.variables

    def is_accepted_symbol(self, symbol: str) -> bool:
        """
        Determine if symbol is an accepted symbol.
        :param symbol: Symbol to evaluate
        :return: True if symbol is an accepted symbol
        """
        return symbol in self.accepted_symbols

    def is_numeral(self, symbol: str) -> bool:
        """
        Determine if symbol is a numeral.
        :param symbol: Symbol to evaluate
        :return: True if symbol is numeral
        """
        return symbol in self.numerals

    def is_operator(self, symbol: str) -> bool:
        """
        Determine if symbol is an operator.
        :param symbol: Symbol to evaluate
        :return: True if symbol is operator
        """
        return symbol in self.operators

    def is_other_symbol(self, symbol: str) -> bool:
        """
        Determine if symbol is a tab, newline, or space.
        :param symbol: Symbol to evaluate
        :return: True if symbol is a tab, newline, or space
        """
        return symbol in self.other_symbols

    def is_variable(self, symbol: str) -> bool:
        """
        Determine if symbol is a variable.
        :param symbol: Symbol to evaluate
        :return: True if symbol is a variable
        """
        return symbol in self.variables
