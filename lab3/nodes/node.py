"""Peter Rasmussen, Lab 3, nodes/node.py

This module provides the Node class, which inherits from the SimpleNode and is one of the parents of
the PolynomialNode class.

"""

# Standard library imports
from typing import Union, Dict

# Local imports
from lab3.nodes.simple_node import SimpleNode


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
