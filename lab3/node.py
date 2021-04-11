"""Peter Rasmussen, Lab 3, node.py

This module provides Node class, which is the building block of the DoublyLinkedCircularList and
PolynomialEvaluator classes.

"""

# Standard library imports
from typing import Union


class SimpleNode:
    """
    Base node for singly-linked list.
    """

class SimpleNode:
    """
    Base node for singly-linked list.
    """

    def __init__(self, name: str, data=None):
        """
        Set name and optionally set data attributes.
        :param data: Node name
        :param data: Node data
        """
        # function arguments
        self.name = name
        self.data = data

        # additional attributes
        self.next_node = None
        self.head = None

    def __str__(self):
        """Return name of node in form of `Node {name}`"""
        return f"Node {self.name}"

    def get_data(self):
        """
        Return node data.
        :return: Node data
        """
        return self.data

    def get_next_node(self):
        """
        Return next node.
        :return: Next node
        """
        return self.next_node

    def set_data(self, new_data):
        """Set node data."""
        self.data = new_data

    def set_next_node(self, new_next_node):
        """
        Set next node
        :param new_next: New next node
        :return: None
        """
        self.next_node = new_next_node


class Node:
    """
    Base node for circular doubly-linked list.
    Includes sign and coef attributes which are used for polynomial expression simplification and
    evaluation.
    """

    def __init__(self, name: str, data=None):
        """
        Set name and optionally set data attributes.
        :param data: Node name
        :param data: Node data
        """
        super().__init__()
        # function arguments
        self.name = name
        self.data = data

        # additional attributes
        self.prev_node = None
        self.tail = None
        self.sign = 1
        self.coef = 1
        self.valid_polynomial: Union[None, bool] = None

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
