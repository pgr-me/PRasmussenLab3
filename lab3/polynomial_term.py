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
        self.term_di = {"coef": 1, "sign": 1}

        # Initialize term as an empty string
        self.term = ""
        self.n_operators = 0
        self.n_symbols = 0
        self.end_of_term = False

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
                self.term_di["sign"] = -1

            # Extract term coefficient
            if self.is_numeral(symbol):
                self.term_di["coef"] = int(symbol)

            # Extract term variable
            if self.is_variable(symbol):
                self.term += symbol

        elif len(self.term) == 1 and self.is_operator(self.term) and self.is_numeral(symbol):
            self.term_di["coef"] = int(symbol)

        # Case when we reach the end of a term and the beginning of a new one
        elif self.is_operator(symbol):
            self.end_of_term = True

        # Otherwise, add symbol to end of term
        else:
            self.term += symbol

    def increment_counts(self, symbol):
        """Increment number of symbols and optionally operator"""
        if self.is_operator(symbol):
            self.n_operators += 1
        self.n_symbols += 1

    def process_term(self) -> dict:
        """
        Compile term into a key-value pair of term and term_di.
        :return: Term dictionary keyed by term.
        """
        return {self.term: self.term_di}

    def reinitialize(self):
        """
        Wipe the object of its data.
        :return: None
        """
        self.term_di = {"coef": 1, "sign": 1}
        self.term = ""
