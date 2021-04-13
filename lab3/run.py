"""Peter Rasmussen, Lab 3, run.py

This module preprocesses an input file of prefix statements, checking each prefix statement for
errors, and then recursively each prefix statement, where possible, into its postfix equivalent.

"""

# standard library imports
import os
from pathlib import Path
from time import time_ns
from typing import Union

# local imports
from lab3.parsers.parse_polynomial_input import parse_polynomial_input
from lab3.parsers.parse_evaluation_input import parse_evaluation_input
from lab3.evaluators.combine import add_expressions
from lab3.tests import tests


def run(
        evaluation_in_file: Path,
        polynomial_in_file: Path,
        out_file: Path,
        file_header: str,
        test: bool
):
    """
    Symbolically combine polynomials and then evaluate for various evaluation sets.
    :param polynomial_in_file: Polynomial input file to read
    :param evaluation_in_file: Evaluation input file to read
    :param out_file: Output file to write to
    :param file_header: Header to add at top of output file
    :param test: True to run tests/test.py
    """

    run_start = time_ns()

    if test:
        tests.main()

    else:
        # Read and parse polynomial input
        polynomial_li = parse_polynomial_input(polynomial_in_file)

        # Read and parse evaluation input
        evaluation_li = parse_evaluation_input(evaluation_in_file)

        node_c = polynomial_li.get_node("C")
        node_d = polynomial_li.get_node("D")
        d_c = node_c.data
        d_d = node_d.data


        d12 = add_expressions(node_c, node_d)

        # Combine polynomial input
        print('here')
        # For each set of evaluation inputs, evaluate polynomials

        # with open(str(out_file), "w") as f:

        #    # Write header to file
        #    write_header(f, file_header, in_file, out_file)

        #    # Convert each line of prefix, as allowed, into postfix equivalents
        #    n_recursive_calls = 0
        #    prefix_converter_elapsed = 0
        #    for line_di in file_di["prefix_data"]:
        #        prefix: list = line_di["prefix"]
        #        line: int = line_di["line"]
        #        f.write(f"Line {line}: Prefix: {array_to_string(prefix)}, ")
        #        prefix_converter = PrefixConverter(symbols.operands, symbols.operators)
        #        if line_di["valid_prefix"]:
        #            postfix = prefix_converter.convert_prefix_to_postfix(prefix)
        #        elif line_di["error"] != "":
        #            postfix = line_di["error"]
        #        else:
        #            postfix = "Nothing to process"
        #        output = f"Postfix: {array_to_string(postfix)}"
        #        f.write(output + os.linesep)
        #        n_recursive_calls += prefix_converter.n_recursive_calls
        #        prefix_converter_elapsed += prefix_converter.elapsed

        #    # compile complexity metrics
        #    lines = file_di["lines"]
        #    run_elapsed = time_ns() - run_start
        #    metrics = {
        #        "run": dict(
        #            lines=lines, elapsed_ns=run_elapsed, lines_per_ns=lines / run_elapsed
        #        ),
        #        "prefix_processor": dict(
        #            elapsed_ns=file_di["elapsed"], lines_per_ns=lines / file_di["elapsed"]
        #        ),
        #        "prefix_converter": dict(
        #            elapsed_ns=prefix_converter_elapsed,
        #            lines_per_ns=lines / prefix_converter_elapsed,
        #            n_recursive_calls=n_recursive_calls,
        #        ),
        #    }

        #    # write footer to file
        #    write_footer(f, metrics)
