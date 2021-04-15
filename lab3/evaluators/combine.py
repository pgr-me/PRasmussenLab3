"""Peter Rasmussen, Lab 3, combine.py

This module performs addition, multiplication, and subtraction operations for polynomial
expressions.

"""

# Standard library imports
from copy import deepcopy
from typing import Union


def add_expressions(node_d1: dict, node_d2: dict, op: str) -> dict:
    """
    Symbolically add two expressions.
    :param node_d1: First node dictionary
    :param node_d2: Second node dictionary
    :return: Dictionary of outputs
    """

    d2 = deepcopy(node_d2)

    # Distribute minus term to node2 data so we can add
    if op == "-":
        for term, di in d2.items():
            di["signed_coef"] *= -1

    # Find intersecting terms
    set_intersection = {k for k in node_d1 if k in d2}

    # Find disjoint terms and combine them
    d = {k: v for k, v in node_d1.items() if k not in d2}
    d2_disjoint = {k: v for k, v in d2.items() if k not in node_d1}
    d.update(d2_disjoint)

    # Combine like terms from intersection set
    for k in set_intersection:
        signed_coef = int(node_d1[k]["signed_coef"]) + int(d2[k]["signed_coef"])
        d[k] = {"signed_coef": signed_coef}

    return d


def concatenate_output_expressions(node_di: dict) -> str:
    """
    Concatenate output polynomial expressions.
    :param node_di: Node dictionary of terms and coefficients
    :return: Concatenated output string of polynomial expressions
    """
    output_expression = ""
    for term, di in node_di.items():
        signed_coef = di["signed_coef"]
        coef_term = f"{str(signed_coef)}{term}"
        if (signed_coef > 0) and output_expression:
            coef_term = f"+{coef_term}"
        output_expression += coef_term
    return output_expression


def multiply_expressions(node_d1, node_d2) -> Union[dict, str]:
    """
    Symbolically multiply expressions.
    :param node_d1: First node to multiply
    :param node_d2: Second node to multiply
    :return: Product node data dict
    """

    # Double for loop to get at the term level
    d = {}
    for term1, di1 in node_d1.items():

        # Iterate over term2
        for term2, di2 in node_d2.items():

            if len(term1) != len(term2):
                return (
                    f"Length of 1st term, {term1}, doesn't equal length of 2nd, {term2}"
                )
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
            d[prod_term] = {"signed_coef": signed_coef}

    return d
