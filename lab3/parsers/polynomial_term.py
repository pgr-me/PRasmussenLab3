"""Peter Rasmussen, Lab 3, parsers/polynomial_term.py

This module provides the PolynomialTerm class, which processes term-level (e.g., -4x2y3z0) strings.

"""

# Standard library imports
from typing import Union

# Local imports
from lab3.symbols import Symbols


class PolynomialTerm(Symbols):
    """
    This class organizes polynomial terms for subsequent processing.
    """

    def __init__(self):
        """
        Construct an empty polynomial term.
        """
        super().__init__()

        # Initialize coefficient to 1 and sign to +1
        self.coef: Union[str, int] = ""
        self.sign = 1
        self.signed_coef: Union[int, None] = None

        # Initialize term as an empty string
        self.term = ""

        # Metrics and record-keeping
        self.n_operators = 0
        self.n_symbols = 0
        self.is_end_of_term = False
        self.orig_term: str = ""
        self.used_variables = set()

        # Error tracking
        self.valid = True
        self.invalid_reason: Union[str, None] = None

    def increment_counts(self, symbol):
        """Increment number of symbols and optionally operator"""
        if self.is_operator(symbol):
            self.n_operators += 1

        # Only increment if we haven't reached the end-of-file
        if symbol:
            self.n_symbols += 1

    def is_multi_numeral_coef(self, symbol: str) -> bool:
        """
        Determine if there is a multi-numeral coefficient in term.
        :param symbol: Symbol to evaluate
        :return: True if multi-numeral coefficient in term
        """
        if self.is_numeral(symbol) and not self.term:
            for i in self.coef:
                if not self.is_numeral(i):
                    return False
            return True
        else:
            return False

    def process_symbol(self, symbol: str):
        """
        Process symbol based on its identity and populate term_di accordingly.
        :param symbol: Symbol to process
        :return: None
        """

        # If end of file is reached, return
        if not symbol:
            return

        # Case when term is empty
        if not self.term:

            # Extract term sign
            if symbol == "-":
                self.sign = -1

            # Extract term coefficient
            if self.is_numeral(symbol):
                self.coef += symbol

            # Extract term variable
            if self.is_variable(symbol):
                self.term += symbol

        # Case when you have a multiple-numeral coefficient
        elif self.is_multi_numeral_coef(symbol):
            self.coef += symbol

        # Case when we reach the end of a term and the beginning of a new one
        elif self.is_operator(symbol) and symbol:
            self.is_end_of_term = True

        # Otherwise, add symbol to end of term
        elif self.is_numeral(symbol) or self.is_variable(symbol):
            self.term += symbol

        # Add variable to set of variables
        if self.is_variable(symbol):
            self.used_variables.add(symbol)

    def process_term(self):
        """
        Prepare term for incorporation into node.
        :return: None.
        """
        if self.coef == "":
            self.coef = 1
        else:
            self.coef = int(self.coef)
        self.signed_coef = self.coef * self.sign

    def reinitialize(self):
        """
        Wipe the object of its data.
        :return: None
        """
        self.coef = ""
        self.sign = 1
        self.term = ""
        self.is_end_of_term = False

    def set_term_as_invalid(self, reason: str):
        """
        Indicate term is invalid and reason why.
        Only indicates reason if the term was theretofore valid.
        :param reason: Why the term is invalid
        :return: None
        """
        if self.valid:
            self.invalid_reason = reason
        self.valid = False

    def validate_symbol(self, symbol: str):
        """
        Validate symbol.
        :return: None
        """
        # If end of file reached, return
        if not symbol:
            return

        # Check if symbol is among accepted symbols
        if not self.is_accepted_symbol(symbol) and not self.is_other_symbol(symbol):
            self.set_term_as_invalid(f"Symbol {symbol} is illegal.")

        # Check if variable is repeated within a term (e.g., xxy2 is not allowed)
        # if self.is_variable(symbol) and symbol in self.used_variables:
        #    self.set_term_as_invalid(f"Variable cannot be repeated in a term.")

    def validate_term(self) -> bool:
        """
        Validate term follows pattern var_1 exp_1 ... var_n exp_n.
        :return: True if term is valid
        """
        ix = 0

        # Empty terms are invalid
        if len(self.term) == 0:
            self.set_term_as_invalid("Terms should not be empty.")
            return self.valid

        # Iterate over term to verify each symbol is as expected
        while ix < len(self.term):
            symbol = self.term[ix]

            # Each even-indexed symbol should be a variable
            if symbol % 2 == 0:
                if not self.is_variable(symbol):
                    self.set_term_as_invalid(
                        "Each even-indexed symbol should be a numeral."
                    )
                    return self.valid

            # Each odd-indexed symbol should be a numeral
            else:
                if not self.is_numeral(symbol):
                    self.set_term_as_invalid(
                        "Each odd-indexed symbol should be a numeral."
                    )
                    return self.valid

            # Final symbol should be a numeral
            if len(self.term) - ix == 1:
                if not self.is_numeral(symbol):
                    self.set_term_as_invalid("Final symbol should be a numeral.")
                    return self.valid

        # Return true if term is valid
        return self.valid
