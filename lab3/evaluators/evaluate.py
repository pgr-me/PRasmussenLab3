"""Peter Rasmussen, Lab 3, evaluate.py

This module parses the evaluation input and uses a two-dimensional singly-linked list (linked list
of linked lists) to store variable: value pairs. Each evaluation term is provided as its own line,
and each term is validated so that it conforms to the pattern variable-value ... variable-value.

"""

# Standard library imports
from pathlib import Path
from typing import Union

# local imports
from lab3.lists.evaluation_input_list import EvaluationList
from lab3.lists.variable_value_list import VariableValueList
from lab3.nodes.variable_value_node import VariableValueNode
from lab3.symbols import Symbols


def parse_evaluation_input(evaluation_in_file: Union[str, Path]) -> EvaluationList:
    """
    Parse polynomial input and organize into PolynomialList, which inherits from CircularList.
    :return: None
    """
    line = 1
    var_val_node = VariableValueNode()
    var_val_li = VariableValueList()
    eval_li = EvaluationList()
    symbols = Symbols()
    with open(evaluation_in_file, "r") as f:

        # While loop adapted from https://www.geeksforgeeks.org/python-program-to-read-character-by-character-from-a-file/
        # Specifically, lines 34 through 37
        while True:

            # Read and preprocess character
            symbol = f.read(1)

            # Record input
            var_val_li.record_input(symbol)

            # Case when we reach end of line or end of file
            end_of_file_or_line = (symbol == "\n") or (not symbol)
            end_of_node = var_val_node.variable is not None and symbols.is_variable(
                symbol
            )

            # Case when we finish populating a node or reach end of line / file
            if end_of_file_or_line or end_of_node:

                # Conditionally process var_val_node
                ready_for_processing = var_val_node.is_ready_for_processing()
                if ready_for_processing:
                    var_val_node.process_node()

                    # Add var_val_node to var_val_li
                    var_val_li.add(var_val_node)

                # Case when we reach end of line or file
                if end_of_file_or_line:

                    # Reverse list so nodes are organized in the order encountered
                    var_val_li.reverse()

                    # Conditionally append var_val_li to eval_li
                    if var_val_li.head is not None:
                        eval_li.append_item(var_val_li)

                    # Re-initialize var_val_node and var_val_li
                    var_val_node = VariableValueNode()
                    var_val_li = VariableValueList()

                    # Increment line number
                    line += 1

                # Case when we finish a node mid-line
                else:

                    # Re-initialize var_val_node
                    var_val_node = VariableValueNode()

                    # Update new node with symbol
                    var_val_node.update_node(symbol)

            # If mid-node, add qualifying symbols to node
            else:
                var_val_node.update_node(symbol)

            # Terminate while loop at end of file
            if not symbol:
                break

    eval_li.stop_timer()

    return eval_li
