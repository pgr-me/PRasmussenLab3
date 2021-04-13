"""Peter Rasmussen, Lab 3, nodes.py

This module provides the SimpleNode, Node, and PolynomialNode classes.
The SimpleNode and PolynomialNode classes are the building blocks of the SinglyLinkedList and
DoublyLinkedCircularList classes used for polynomial simplification and evaluation.

"""

# Standard library imports
from time import time_ns
from typing import Union, Dict

# Local imports
from lab3.polynomial_term import PolynomialTerm
from lab3.utils import Timer


class SimpleNode:
    """
    Base node for singly-linked list.
    """

    def __init__(self, name: str, data=None):
        """
        Set name and optionally set data attributes.
        :param data: PolynomialNode name
        :param data: PolynomialNode data
        """
        # function arguments
        self.name = name
        self.data = data

        # additional attributes
        self.next_node = None
        self.head = None

    def __str__(self):
        """Return name of node in form of `PolynomialNode {name}`"""
        return f"PolynomialNode {self.name}"

    def get_data(self):
        """
        Return node data.
        :return: PolynomialNode data
        """
        return self.data

    def get_next_node(self):
        """
        Return next node.
        :return: Next node
        """
        return self.next_node

    def set_data(self, new_data):
        """
        Set node data.
        :param new_data: PolynomialNode data
        :return: None
        """
        """Set node data."""
        self.data = new_data

    def set_next_node(self, new_next_node):
        """
        Set next node
        :param new_next_node: New next node
        :return: None
        """
        self.next_node = new_next_node


class Node(SimpleNode):
    """
    Base node for circular doubly-linked list.
    """

    def __init__(self, name: str, datatype: Union[dict, int, str] = dict):
        """
        Set name and optionally set data attributes.
        :param name: Node name
        :param datatype: Node datatype (i.e., dict, int, or str)
        """
        super().__init__(name, datatype)

        # function arguments
        self.name = name
        self.datatype = datatype
        if datatype not in [dict, str, int]:
            raise TypeError("datatype {datatype} not one of dict, int, or str.")
        self.data = None

        # additional attributes
        self.prev_node = None
        self.tail = None

    def get_prev_node(self):
        """
        Get previous node.
        :return: Previous node
        """
        return self.prev_node

    def set_prev_node(self, new_prev_node):
        """
        Set next node
        :param new_prev_node: New prev node
        :return: None
        """
        self.prev_node = new_prev_node


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
        self.echoed_string = ""

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
        self.echoed_string = ""

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

    def record_symbol(self, symbol: str):
        if symbol:
            self.echoed_string += symbol
