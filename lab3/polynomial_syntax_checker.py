"""Peter Rasmussen, Lab 3, polynomial_syntax_checker.py

This module provides the PolynomialSyntaxError and PolynomialSyntaxChecker classes. The
PolynomialSyntaxChecker class catches the first error encountered in a polynomial string, ignoring
subsequent errors for the sake of simplicity. This class is used by the make_polynomial_list module.

Polynomial statements with syntax errors are not simplified nor evaluated. Instead, an error message
encapsulated in PolynomialSyntaxError object is written in lieu of the would-have-been outputs.

This module was not integrated into polynomial_term and node modules is because it spans the term
and node levels, and therefore I decided it belonged as its own module.

"""

# Local imports
from lab3.symbols import Symbols


class PolynomialSyntaxError(Exception):
    """Exception to capture polynomial syntax errors."""

    pass


class PolynomialSyntaxChecker(Symbols):
    """
    This class checks polynomial syntax.
    Methods are organized in a top-down fashion: highest-level methods come first, static methods
    come last.
    For readability, we only capture the first error in a polynomial term.
    """

    def __init__(self):
        """
        Initialize operands and operators.
        :param None
        """
        super().__init__()
        self.used_node_names = set()
        self.used_numerals = set()
        self.error = ""

    def check_if_leading_zero(self, numeral_str: str, column: int):
        """
        True if a numeral sequence (123) begins with a leading zero.
        :param numeral_str: String of consecutive numerals (e.g., 123)
        :param column: Current column number of line
        """
        if not self.no_prior_error():
            return

        try:
            if numeral_str[0] == '0':
                error_message = f"Column {column}: Numeral sequence begins with a leading zero."
                raise PolynomialSyntaxError(error_message)
        except PolynomialSyntaxError as e:
            self.error = e.__repr__()

    def check_if_legal_symbol(self, character: str, column: int):
        """
        Check if symbol is legal (i.e., among accepted symbols).
        :param character: Symbol to check.
        :param column: Line column number.
        """
        try:
            if self.no_prior_error() and not self.is_accepted_symbol(character):
                error_message = (
                    f"Illegal character `{character}` found in column {column}"
                )
                raise PolynomialSyntaxError(error_message)
        except PolynomialSyntaxError as e:
            self.error = e.__repr__()

    def is_accepted_symbol(self, symbol: str) -> bool:
        """
        Determine if symbol is an accepted operand, operator, or other accepted symbol.
        :param symbol: Symbol to evaluate
        :return: True if symbol is accepted
        """
        return (
                self.is_operand(symbol) | self.is_operator(symbol) | self.is_other(symbol)
        )

    def is_numeral(self, symbol: str) -> bool:
        """
        Determine if symbol is a numeral.
        :param symbol: Symbol to evaluate
        :return: True if symbol is a numeral
        """
        return symbol in self.numerals

    def is_operator(self, symbol: str) -> bool:
        """
        Determine if symbol is an accepted operator.
        :param symbol: Symbol to evaluate
        :return: True if symbol is an accepted operator
        """
        return symbol in self.operators

    def is_other(self, symbol: str) -> bool:
        """
        Determine if symbol is another accepted - yet non-operator, non-operand - symbol.
        :param symbol: Symbol to evaluate
        :return: True if accepted other symbol
        """
        return symbol in self.other_symbols

    def no_prior_error(self) -> bool:
        """Check if there has been no error.
        :param: None
        :return: True if no previous error encountered.
        """
        return self.error == ""

    @staticmethod
    def is_empty(li: list) -> bool:
        """
        Determine whether string contains any numerals or operators.
        The string is "empty" if it only contains spaces and tabs.
        :param li: List of character counts by class
        :return: True if string contains zero elements of interest
        """
        n = 0
        for i in li:
            n += i
        return n == 0

