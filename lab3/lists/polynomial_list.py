"""Peter Rasmussen, Lab 3, lists/polynomial_list.py

This module provides PolynomialList class, which is a doubly-linked circular list and serves as the
parent class for the PolynomialEvaluator class.

"""

# Standard library imports
from typing import Union

# Local imports

# Local imports
from lab3.lists.circular_list import CircularList


class PolynomialList(CircularList):
    """CircularList modified for polynomial simplification and evaluation."""

    def __init__(self):
        """Construct an empty doubly-linked circular list."""
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
