"""Peter Rasmussen, Lab 3, utils.py

This module provides miscellaneous utility functions used by other modules.

"""

# standard library imports
from time import time_ns
from typing import Union


class Timer:
    """Measure elapsed time."""
    def __init__(self):
        self.start: int = time_ns()
        self.stop: Union[int, None] = None
        self.elapsed: Union[int, None] = None

    def stop_timer(self) -> int:
        """
        Stop timer and compute elapsed time.
        :return: Elapsed time
        """
        self.stop = time_ns()
        self.elapsed = self.stop - self.start
        return self.elapsed


def array_to_string(a: list) -> str:
    """
    Convert an array to a string.
    :param a: List of elements
    :return: String of concatenated elements
    """
    s = ""
    for i in a:
        s += i
    return s


def copy_list(in_li: list)->list:
    """
    Make a deep copy of a list.
    :param in_li: Input list
    :return: Deep copy of output list
    """
    out_li = []
    for i in in_li:
        out_li.append(i)
    return out_li
