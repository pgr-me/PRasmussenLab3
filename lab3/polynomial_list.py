"""Peter Rasmussen, Lab 3, polynomial_list.py

This module provides PolynomialList class, which is a doubly-linked circular list and serves as the
parent class for the PolynomialEvaluator class.

"""

# Standard library imports
from typing import Callable, Union

# Local imports
from lab3.nodes import PolynomialNode

# Local imports
from lab3.circular_list import CircularList


class PolynomialList(CircularList):
    """CircularList modified for polynomial simplification and evaluation."""

    def __init__(self):
        """Construct an empty doubly-linked circular list."""
        super().__init__()

    def validate_node_variables(self):
        for name in self.names:
            node = self.get_node(name)
            if node.

