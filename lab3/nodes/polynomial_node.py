"""Peter Rasmussen, Lab 3, polynomial_node.py

This module provides the SimpleNode, Node, and PolynomialNode classes.
The SimpleNode and PolynomialNode classes are the building blocks of the SinglyLinkedList and
DoublyLinkedCircularList classes used for polynomial simplification and evaluation.

"""

# Standard library imports
from time import time_ns
from typing import Union, Dict

# Local imports
from lab3.nodes.node import Node
from lab3.parsers.polynomial_term import PolynomialTerm
from lab3.utils import Timer


class PolynomialNode(Node, Timer):
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
        self.data: Dict[str, Dict[str, int]] = {}
        self.echoed_input = ""

        # metrics
        self.valid: bool = True
        self.n_terms = 0
        self.invalid_reason: Union[str, None] = None
        self.invalid_term: Union[str, None] = None
        self.start: int = time_ns()
        self.stop: Union[int, None] = None
        self.elapsed: Union[int, None] = None
        self.columns = 0
        self.line: Union[int, None] = None
        self.echoed_input = ""

    def increment_columns(self, symbol):
        """
        Increment column number.
        :return:
        """
        # Only increment if symbol is not end-of-file symbol
        if symbol:
            self.columns += 1

    def set_line(self, line):
        """
        Set line number
        :return: None
        """
        self.line = line

    def update_node(self, pt: PolynomialTerm):
        """
        Update node data using polynomial term data.
        :param pt: Polynomial term object to add to / merge into dictionary
        :return: None
        """
        if type(pt) != PolynomialTerm:
            raise TypeError("Must supply a polynomial term of type PolynomialTerm.")

        # If term is empty, don't update the node with it
        if pt.term == "":
            return

        # If the term is a duplicate, we need to combine the new term with the current one
        if pt.term in self.data:
            current_sign = self.data[pt.term]["sign"]
            current_coef = self.data[pt.term]["coef"]
            self.data[pt.term]["coef"] = (
                    current_sign * current_coef + pt.sign * pt.coef
            )

            # Account for sign changes
            if self.data[pt.term]["coef"] < 0:
                self.data[pt.term]["sign"] = -1
                self.data[pt.term]["coef"] *= -1
            elif (self.data[pt.term]["coef"] > 0) and (
                    self.data[pt.term]["sign"] < 0
            ):
                self.data[pt.term]["sign"] = 1

            # Remove term if sum of its parts sum yields coefficient of zero
            elif self.data[pt.term]["coef"] == 0:
                self.data.pop(pt.term, None)

        # If term is new, simply add it to dictionary
        else:
            self.data[pt.term] = {"coef": pt.coef, "sign": pt.sign}

        # Recompute number of terms
        self.n_terms = len(self.data)

        # Determine if node is valid: if any term is invalid then node is invalid
        self.valid = self.valid & pt.valid

        # If invalid set reason for it
        if not self.valid and self.invalid_reason is None:
            self.invalid_reason = pt.invalid_reason

        # Add signed coefficient term
        coef = self.data[pt.term]["coef"]
        sign = self.data[pt.term]["sign"]
        self.data[pt.term]["signed_coef"] = sign * coef

    def record_symbol(self, symbol: str):
        if symbol and symbol != '\n':
            self.echoed_input += symbol
