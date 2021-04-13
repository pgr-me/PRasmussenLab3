"""Peter Rasmussen, Lab 3, combine.py

This module parses the evaluation input and uses a two-dimensional singly-linked list (linked list
of linked lists) to store variable: value pairs. Each evaluation term is provided as its own line,
and each term is validated so that it conforms to the pattern variable-value ... variable-value.

"""

# standard library imports
from pathlib import Path
from typing import Union

# local imports
from lab3.nodes.polynomial_node import PolynomialNode


def add_expressions(node1: PolynomialNode, node2: PolynomialNode) -> dict:
    """
    Symbolically add two expressions.
    :param node1: First node
    :param node2: Second node
    :return: Dictionary of outputs
    """
    # Extract dictionaries from nodes
    d1 = node1.data
    d2 = node2.data

    # Find intersecting terms
    set_intersection = {k for k in d1 if k in d2}

    # Find disjoint terms and combine them
    d = {k: v for k, v in d1.items() if k not in d2}
    d2_disjoint = {k: v for k, v in d2.items() if k not in d1}
    d.update(d2_disjoint)

    # Combine like terms from intersection set
    for k in set_intersection:
        d[k] = d1[k]["signed_coef"] + d2[k]["signed_coef"]

    return d
