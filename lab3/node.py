"""Peter Rasmussen, Lab 3, node.py

This module provides Node class, which is the building block of the DoublyLinkedCircularList and
PolynomialList classes.

"""


class Node:
    """
    Base node for circular doubly-linked list.
    Includes sign and coef attributes which are used for polynomial expression simplification and
    evaluation."""

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
        self.prev_node = None
        self.head = None
        self.tail = None
        self.sign = 1
        self.coef = 1

    def __str__(self):
        """Return name of node in form of `Node {name}`"""
        return f"Node {self.name}"
