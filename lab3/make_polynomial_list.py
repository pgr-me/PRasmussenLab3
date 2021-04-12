"""Peter Rasmussen, Lab 3, make_polynomial_list.py

This module provides the PrefixPreProcessor class, which reads a file of prefix statements character
by character and checks each prefix statement for errors. PrefixPreProcessor.preprocess_prefix_input
returns a list of dictionaries. Each dictionary corresponds to one line in the input file and
contains prefix statements, errors (if any), and complexity metrics. This module uses the
syntax_checker module to catch prefix syntax errors.

"""

# standard library imports
from pathlib import Path
from time import time_ns
from typing import Union

# local imports
from lab3.polynomial_syntax_checker import PolynomialSyntaxChecker
from lab3.circular_list import CircularList
from lab3.nodes import PolynomialNode
from lab3.utils import copy_list
from lab3.symbols import Symbols
from lab3.polynomial_term import PolynomialTerm


# from lab3.polynomial_evaluator import PolynomialEvaluator

class PolynomialParser:
    """
    This class converts prefix expressions into postfix equivalents.
    Methods are organized top-down: highest-level methods come first, static methods come last.
    """

    def __init__(self, polynomial_in_file: Union[str, Path]):
        """
        Initialize input file, operands, and operators.
        :param polynomial_in_file: Input file to read
        """
        self.polynomial_in_file = Path(polynomial_in_file)
        self.file_di = {
            "start": time_ns(),
            "stop": None,
            "symbols": 0,
            "lines": 0,
            "line_level_data": [],
        }

    def parse_polynomial_input(self) -> dict:
        """
        Convert prefix input from file, echoing inputs and postfix conversions to output file.
        :return: Echoed prefix with corresponding postfix equivalents; summary stats at file bottom
        """
        line = 1
        column = 0
        line_di = self.make_line_di(line)
        syntax_checker = PolynomialSyntaxChecker()
        cir_li = CircularList()
        node = PolynomialNode()
        polynomial_term = PolynomialTerm()
        with open(self.polynomial_in_file, "r") as f:

            # While loop adapted from https://www.geeksforgeeks.org/python-program-to-read-character-by-character-from-a-file/
            # Specifically, lines 61 through 63
            # The while loop iterates at the character level
            # Initialize symbol and line dict

            while True:

                # Read and preprocess each character
                symbol = f.read(1)
                column += 1
                syntax_checker.check_if_legal_symbol(symbol, column)
                polynomial_term.increment_counts(symbol)

                # If we reach the end of the line, populate file_di and re-initialize line_di
                if (symbol == "\n") or (not symbol):
                    line_di["line"] = line

                    li = [line_di["n_variables"], line_di["n_numerals"], line_di["n_operators"]]
                    line_di["is_empty"] = syntax_checker.is_empty(li)

                    # Determine validity of polynomial
                    if syntax_checker.no_prior_error() and not node.n_terms > 0:
                        line_di["valid_polynomial"] = True
                    else:
                        line_di["valid_polynomial"] = False

                    # Insert into circular list and reinitialize node
                    node.data = node_data_di
                    cir_li.insert(node, direction="right")
                    node_name = node_names[node_number]
                    node = PolynomialNode(node_name)
                    node_number += 1

                    # Append line_di to file_di, re-initialize line dict, and reset error
                    line_di["stop"] = time_ns()
                    line_di["elapsed"] = line_di["stop"] - line_di["start"]
                    self.file_di["line_level_data"].append(line_di)
                    line += 1
                    line_di = self.make_line_di(line)
                    syntax_checker.error = ""

                else:
                    line_di["column"] += 1  # Increment column count
                    syntax_checker.check_if_legal_symbol(symbol, line_di["column"])
                    polynomial_term.process_symbol(symbol)

                    # Case when end of term is reached: populate node_data_di and reinitialize term
                    if polynomial_term.end_of_term:
                        node_data_di[polynomial_term.term] = polynomial_term.
                        polynomial_term.reinitialize()
                        polynomial_term.process_symbol(symbol)

                # Terminate while loop at end of file
                if not symbol:
                    break

            # After reaching end of file, compute total time complexity and return the file_di
            self.file_di["stop"] = time_ns()
            self.file_di["elapsed"] = self.file_di["stop"] - self.file_di["start"]
            self.file_di["lines"] = line
            return self.file_di

    @staticmethod
    def make_line_di(line) -> dict:
        """
        Make a dictionary that line that contains complexity metrics, line number, prefix, and, if
        applicable, and error encountered during syntax checking.
        :return: Line-level dictionary of preprocessed prefix outputs
        """
        return {
            "start": time_ns(),
            "stop": None,
            "elapsed": None,
            "prefix": [],
            "n_numerals": 0,
            "n_variables": 0,
            "n_operators": 0,
            "line": line,
            "column": 0,
            "is_empty": None,
            "error": "",
        }
