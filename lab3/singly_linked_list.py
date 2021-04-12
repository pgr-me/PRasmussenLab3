"""Peter Rasmussen, Lab 3, circular_list.py

This module provides SinglyLinkedList class, which the PolynomialEvaluator class uses to hold
polynomials.

"""

# Standard library imports
from typing import Union

# Local imports
from lab3.nodes import PolynomialNode, SimpleNode


class SinglyLinkedList:
    """Singly linked list."""

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self) -> bool:
        """
        Determine if list is empty
        :return: True if list is empty
        """
        return self.head is None

    def add(self, node):
        """
        Add node to end of list.
        :param node: PolynomialNode to add
        :return: None
        """
        if type(node) not in [SimpleNode, PolynomialNode]:
            raise TypeError('Can only add object of type SimpleNode.')

        node.set_next_node(self.head)
        self.size += 1
        self.head = node

    def valid_rank(self, rank) -> bool:
        """
        Check if node is valid.
        Function code based on material presented in lecture notes.
        :param rank: Rank of node
        :return: True if valid rank
        """
        return (rank >= 1) & (rank <= self.size)

    def ptr_to(self, rank) -> Union[SimpleNode, PolynomialNode]:
        """
        Return pointer to node of specified rank.
        Function code based on material presented in lecture notes.
        """
        if self.valid_rank(rank):
            here = self.head
            for i in range(1, rank):
                here = here.next_node
            return here
        else:
            raise IndexError('Rank out of range.')

    def delete(self, rank) -> Union[SimpleNode, PolynomialNode]:
        """
        Delete node from linked list.
        Function code based on material presented in lecture notes.
        """
        if self.size == 0:
            raise ValueError('Cannot delete from empty list.')
        if not self.valid_rank(rank):
            raise IndexError('Rank out of range.')
        else:
            if rank == 1:
                temp = self.head
                self.head = temp.next_node
            else:
                after: SimpleNode = self.ptr_to(rank - 1)
                temp = after.next_node
                after.next_node = temp.next_node
            self.size -= 1
            temp.next_node = None
        return temp.data

    def insert(self, node, rank) -> None:
        """
        Insert node into linked list after item of specified rank.
        Function code based on material presented in lecture notes.
        """
        if type(node) not in [SimpleNode, PolynomialNode]:
            raise TypeError('node must be of type SimpleNode.')
        self.size += 1  # Increase size by 1

        # Insert at front of list if rank is 1
        if rank == 1:
            node.next_node = self.head
            self.head = node

        # Otherwise
        else:
            after = self.ptr_to(rank - 1)  # Get reference to before node
            node.next_node = after.next_node  # Connect to tail
            after.next_node = node  # Connect head to node

    def display(self) -> None:
        """
        Display construction of linked list.
        """
        print(f'Head: {self.head}')
        temp = self.head
        for i in range(1, self.size + 1):
            print(f'Rank {i}, {temp}, Next: {temp.next_node}')
            temp = temp.next_node

    def reverse(self) -> None:
        """
        Reverse linked list.
        Solution informed by https://www.geeksforgeeks.org/reverse-a-linked-list/
        """
        before = None
        current = self.head

        # Iterate over each item in linked list
        for i in range(1, self.size + 1):

            # Set aside after pointer
            after = current.next_node

            # Reverse pointer for current
            current.next_node = before

            # Update before and current
            before = current
            current = after

        # Redefine head
        self.head = before
