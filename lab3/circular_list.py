"""Peter Rasmussen, Lab 3, circular_list.py

This module provides Node, PolynomialNode, and CircularList classes.

"""

# Standard library imports
from typing import Callable, Union

# Local imports
from node import Node


class DoublyLinkedCircularList:
    """Doubly-linked circular list."""

    def __init__(self):
        """Construct an empty doubly-linked circular list."""
        self.head = None
        self.tail = None
        self.size = 0
        self.names = set()

    def insert(self, new_node: Node, direction: str) -> None:
        """Insert item to the left of the header."""

        # Verify direction is either right or left
        if direction not in ['right', 'left']:
            raise ValueError("Direction {direction} must equal 'right' or 'left'.")

        # Verify new node is unique: if so, add node to names
        if new_node.name in self.names:
            raise ValueError("Node {new_node.get_name()} is a duplicate.")
        else:
            self.names.add(new_node.name)

        # Case when list is empty
        if self.head is None:
            new_node.next_node = new_node
            new_node.prev_node = new_node
            self.head = new_node
            self.tail = new_node

        # Case when list is not empty
        else:

            # Insert to the right
            if direction == 'right':
                prev_node = self.tail
                new_node.prev_node = prev_node
                new_node.next_node = self.head
                prev_node.next_node = new_node
                self.head.prev_node = new_node
                self.tail = new_node

            # Insert to left
            else:
                next_node = self.head
                new_node.next_node = next_node
                new_node.prev_node = self.tail
                next_node.prev_node = new_node
                self.tail.next_node = new_node
                self.head = new_node

        self.size += 1

    def get_node(self, node_name: str):
        """Return node if found."""

        cur_node = self.head
        # Return cur_node if its name matches provided name
        if cur_node.name == node_name:
            return cur_node
        cur_node = cur_node.next_node
        while cur_node != self.head:
            if cur_node.name == node_name:
                return cur_node
            cur_node = cur_node.next_node

        return None

    def is_head(self, node: Node):
        """True if head points to node."""
        return node == self.head

    def is_tail(self, node: Node):
        """True if tail points to node."""
        return node == self.tail

    def merge_nodes(self, left_node_name: str, right_node_name: str, f: Callable):
        """Merge left node into right node."""

        if self.size == 0:
            print("Cannot merge on an empty list.")

        elif self.size == 1:
            print("Cannot merge one node.")

        elif left_node_name not in self.names:
            print(f"Left node {left_node_name} not among nodes.")

        elif right_node_name not in self.names:
            print(f"Right node {right_node_name} not among nodes.")

        else:
            left_node = self.get_node(left_node_name)
            right_node = self.get_node(right_node_name)

            if left_node.next_node != right_node:
                print("Node {left_node.name} is not to left of {right_node.name}")

            else:
                right_node.name = f"{left_node.name}{right_node.name}"
                right_node.data = f(left_node, right_node)
                self.remove(left_node_name)

    def remove(self, node_name: Union[str, int]):
        """
        Remove node.
        """
        if type(node_name) not in [str, int]:
            raise TypeError("Node names must either be integer or string.")

        elif self.size == 0:
            print("Cannot remove a node from an empty list.")

        elif node_name not in self.names:
            print(f"Node {node_name} not among nodes in list.")

        # Case when list is not empty and node is present
        else:
            node = self.get_node(node_name)

            # If only one node, simply set head and tail to None
            if self.size == 1:
                self.head = None
                self.tail = None

            # Case when there is more than one node
            else:
                is_head = self.is_head(node)
                is_tail = self.is_tail(node)

                prev_node = node.prev_node
                suc_node = node.next_node

                prev_node.next_node = suc_node
                suc_node.prev_node = prev_node

                if is_head:
                    self.head = suc_node

                elif is_tail:
                    self.tail = prev_node

            self.names.remove(node_name)
            self.size -= 1

    def search(self, node_name: str):
        """
        True if node found.
        """
        return node_name in self.names

    def traverse(self, data: bool = False) -> None:
        """Traverse the circular list left to right, from head to tail, and print each element along the way."""

        if self.head is not None:
            cur_node = self.head
            counter = 0
            print_statement = []
            while counter < self.size:
                line = []
                if cur_node == self.head:
                    line.append("Head")
                if cur_node == self.tail:
                    line.append("Tail")
                line.append(f"\tNode {cur_node.name}")
                if data:
                    line.append(f": {cur_node.data}")
                print_statement.append(" ".join(line))

                cur_node = cur_node.next_node
                counter += 1

            print("\n".join(print_statement))

        else:
            print("Empty list: nothing to traverse.")
