"""Peter Rasmussen, Lab 3, parse_polynomial_input.py

This module provides the PrefixPreProcessor class, which reads a file of prefix statements character
by character and checks each prefix statement for errors. PrefixPreProcessor.preprocess_prefix_input
returns a list of dictionaries. Each dictionary corresponds to one line in the input file and
contains prefix statements, errors (if any), and complexity metrics. This module uses the
syntax_checker module to catch prefix syntax errors.

"""

# standard library imports
from pathlib import Path
from typing import Union

# local imports
from lab3.nodes import PolynomialNode
from lab3.polynomial_list import PolynomialList
from lab3.polynomial_term import PolynomialTerm


def parse_polynomial_input(polynomial_in_file: Union[str, Path]) -> PolynomialList:
    """
    Parse polynomial input and organize into PolynomialList, which inherits from CircularList.
    :return: None
    """
    line = 1
    term = PolynomialTerm()
    node = PolynomialNode()
    li = PolynomialList()
    with open(polynomial_in_file, "r") as f:

        # While loop adapted from https://www.geeksforgeeks.org/python-program-to-read-character-by-character-from-a-file/
        # Specifically, lines 56 through 59
        while True:

            # Read and preprocess character
            symbol = f.read(1)
            term.increment_counts(symbol)
            term.validate_symbol(symbol)
            term.process_symbol(symbol)
            node.increment_columns(symbol)
            node.record_symbol(symbol)
            print(symbol)
            # Case when we reach end of line or end of file
            if (symbol == "\n") or (not symbol):

                # Update node and list line numbers
                node.set_line(line)
                li.set_line(line)

                # Update node with term data
                term.process_term()
                node.update_node(term)
                node.stop_timer()

                # Insert node into circular list
                if node.data != {}:
                    li.insert(node, direction="right")

                # Re-initialize term and node
                term.reinitialize()
                node = PolynomialNode()

                # Increment line number
                line += 1

            # Case when we reach the end of a term
            elif term.is_end_of_term:

                # Update node
                term.process_term()
                node.update_node(term)
                print(f"\tTerm: {term.term}")
                # Re-initialize term
                term.reinitialize()

                # Process operator for next term
                term.process_symbol(symbol)

            # Terminate while loop at end of file
            if not symbol:
                li.validate_variables()
                break

    li.stop_timer()

    return li
