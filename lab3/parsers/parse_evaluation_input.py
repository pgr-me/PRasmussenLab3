"""Peter Rasmussen, Lab 3, parse_evaluation_input.py

This module parses the evaluation input and uses a two-dimensional singly-linked list (linked list
of linked lists) to store variable: value pairs. Each evaluation term is provided as its own line,
and each term is validated so that it conforms to the pattern variable-value ... variable-value.

"""

# standard library imports
from pathlib import Path
from typing import Union

# local imports
from lab3.lists.evaluation_lists import EvaluationList, ValuesList


def parse_evaluation_input(evaluation_in_file: Union[str, Path]) -> None:
    """
    Parse polynomial input and organize into PolynomialList, which inherits from CircularList.
    :return: None
    """
    line = 1
    values_li = ValuesList()
    eval_li = EvaluationList()
    values_node =
    with open(evaluation_in_file, "r") as f:

        # While loop adapted from https://www.geeksforgeeks.org/python-program-to-read-character-by-character-from-a-file/
        # Specifically, lines 56 through 59
        while True:

            # Read and preprocess character
            symbol = f.read(1)
            values_li.insert()
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
