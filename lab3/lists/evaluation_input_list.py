"""Peter Rasmussen, Lab 3, evaluation_input_list.py

This module provides the list evaluation classes EvaluationList and VariableValueList. EvaluationList is a
list of VariableValueList lists. Both classes inherit from the SinglyLinkedList class.

"""

# Standard library imports
from typing import Union

# Local imports
from lab3.lists.array import Array
from lab3.utils import Timer


class EvaluationList(Array, Timer):
    """Singly-linked list modified for polynomial evaluation."""

    def __init__(self):
        """Construct an empty list."""
        super().__init__()

        # metrics
        self.line: Union[int, None] = 0

    def set_line(self, line: int):
        """
        Set line number.
        :return:
        """
        self.line = line
