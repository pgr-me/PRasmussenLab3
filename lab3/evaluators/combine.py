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


def multiply_expressions(node1, node2) -> Union[dict, str]:
    """
    Symbolically multiply expressions.
    :param node1: First node to multiply
    :param node2: Second node to multiply
    :return: Product node data dict
    """
    data_di1 = node1.data
    data_di2 = node2.data

    # Double for loop to get at the term level
    d = {}
    for term1, di1 in data_di1.items():
        print(f"Term 1: {term1}")

        # Iterate over term2
        for term2, di2 in data_di2.items():
            print(f"\tTerm 2: {term2}")
            if len(term1) != len(term2):
                return f"Length of 1st term, {term1}, doesn't equal length of 2nd, {term2}"
            if len(term1) % 2 != 0:
                return "There is a variable-power imbalance in the terms: ratio must be 1:1"

            # While loop to get to the symbol level
            var_ix = 0
            prod_term = ""
            while var_ix < len(term1) - 1:
                pow_ix = var_ix + 1
                var1, var2 = term1[var_ix], term2[var_ix]
                if var1 != var2:
                    return f"Variable {var1} in term {term1} does not equal variable {var2} in term {term2}"
                pow1, pow2 = term1[pow_ix], term2[pow_ix]
                pow_ = str(int(pow1) + int(pow2))
                var_pow = var1 + pow_
                prod_term += var_pow
                var_ix += 2

            # Obtained signed coefficient product
            signed_coef = di1["signed_coef"] * di2["signed_coef"]

            # Add product-term: signed coefficient pair to dictionary
            d[prod_term] = signed_coef

    return d
