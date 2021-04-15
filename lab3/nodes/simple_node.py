"""Peter Rasmussen, Lab 3, nodes/simple_node.py

This module provides the SimpleNode class, and is the node used by the SinglyLinkedList class.

"""


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
