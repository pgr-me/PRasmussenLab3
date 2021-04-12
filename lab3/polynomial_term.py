"""Peter Rasmussen, Lab 3, polynomial_term.py

This module provides the PolynomialTerm class, which processes term-level (e.g., -4x2y3z0) strings.

"""

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
        self.coef = 1
        self.sign = 1

        # Initialize term as an empty string
        self.term = ""
        self.n_operators = 0
        self.n_symbols = 0
        self.end_of_term = False

    def increment_counts(self, symbol):
        """Increment number of symbols and optionally operator"""
        if self.is_operator(symbol):
            self.n_operators += 1
        self.n_symbols += 1

    def process_symbol(self, symbol: str):
        """
        Process symbol based on its identity and populate term_di accordingly.
        :param symbol: Symbol to process
        :return: None
        """

        # Case when term is empty
        if not self.term:
            # Extract term sign
            if symbol == "-":
                self.sign = -1

            # Extract term coefficient
            if self.is_numeral(symbol):
                self.coef = int(symbol)

            # Extract term variable
            if self.is_variable(symbol):
                self.term += symbol

        elif len(self.term) == 1 and self.is_operator(self.term) and self.is_numeral(symbol):
            self.coef = int(symbol)

        # Case when we reach the end of a term and the beginning of a new one
        elif self.is_operator(symbol):
            self.end_of_term = True

        # Otherwise, add symbol to end of term
        else:
            self.term += symbol

    def process_term(self) -> dict:
        """
        Compile term into a key-value pair of term and term_di.
        :return: Term dictionary keyed by term.
        """
        return {self.term: {"coef": self.coef, "sign": self.sign}}

    def reinitialize(self):
        """
        Wipe the object of its data.
        :return: None
        """
        self.coef = 1
        self.sign = 1
        self.term = ""

    def is_term_valid(self) -> bool:
        """
        Validate term follows pattern var_1 exp_1 ... var_n exp_n.
        :return: True if term is valid
        """
        valid = True
        ix = 0

        # Empty terms are invalid
        if len(self.term) == 0:
            return False

        # Iterate over term to verify each symbol is as expected
        while ix < len(self.term):
            symbol = self.term[ix]

            # Each even-indexed symbol should be a variable
            if symbol % 2 == 0:
                if not self.is_variable(symbol):
                    return False

            # Each odd-indexed symbol should be a numeral
            else:
                if not self.is_numeral(symbol):
                    return False

            # Final symbol should be a numeral
            if len(self.term) - ix == 1:
                if not self.is_numeral(symbol):
                    return False

        # Return true if term is valid
        return True
