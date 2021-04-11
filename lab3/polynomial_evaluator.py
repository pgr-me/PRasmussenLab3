"""Peter Rasmussen, Lab 3, polynomial_list.py

This module provides the PolynomialList class, which inherits from the CircularList class.
PolynomialList is used for polynomial simplification and evaluation.

"""

# Standard library imports
from typing import Callable, Union

# Local imports
from circular_list import CircularList


class PolynomialList(CircularList):
    """Doubly-linked circular list customized for polynomial simplification and evaluation."""

    def __init__(self):
        super().__init__()

    def merge_nodes(
        self, left_node_name: str, right_node_name: str, f: Callable
    ) -> bool:
        """
        Merge left node into right node.
        :param left_node_name: Left node name
        :param right_node_name: Right node name
        :param f: Function to process merged node data
        :return: True if nodes successfully merged
        """

        if self.size == 0:
            print("Cannot merge on an empty list.")
            return False
        elif self.size == 1:
            print("Cannot merge one node.")
            return False
        elif left_node_name not in self.names:
            print(f"Left node {left_node_name} not among nodes.")
            return False
        elif right_node_name not in self.names:
            print(f"Right node {right_node_name} not among nodes.")
            return False
        else:
            left_node = self.get_node(left_node_name)
            right_node = self.get_node(right_node_name)
            if left_node.next_node != right_node:
                print("Node {left_node.name} is not to left of {right_node.name}")
                return False
            else:
                right_node.name = f"{left_node.name}{right_node.name}"
                right_node.data = f(left_node, right_node)
                self.remove_node(left_node_name)
                return True