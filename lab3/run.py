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
from lab3.polynomial_operations import polynomial_operations
from lab3.evaluators.combine import add_expressions, concatenate_output_expressions, multiply_expressions
from lab3.symbols import Symbols
from lab3.tests import tests
from lab3.utils import write_header, write_footer


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
        symbols = Symbols()

        # Initialize output content, which we'll write to output file
        output_content = ""

        # Read and parse polynomial input
        polynomial_li = parse_polynomial_input(polynomial_in_file)

        # Read and parse evaluation input
        evaluation_li = parse_evaluation_input(evaluation_in_file)

        # Write each input polynomial expression
        output_content += "\nPolynomial input expression definitions\n"
        for node_name in symbols.node_names:
            if node_name in polynomial_li.names:
                input_polynomial_expression = polynomial_li.get_node(node_name).echoed_input
                output_content += f"{node_name} = {input_polynomial_expression}\n"

        # For each set of evaluation inputs, evaluate polynomials
        output_content += "\nPolynomial expression simplification and evaluation\n"
        for polynomial_operation in polynomial_operations:

            # Extract node data from polynomial list
            node_label1, op, node_label2 = polynomial_operation
            node1 = polynomial_li.get_node(node_label1)
            node2 = polynomial_li.get_node(node_label2)

            # Echo operation (e.g., A + B)
            output_content += f"{polynomial_operation}\n"

            # Echo polynomial expression input
            input_expression = f"Input:\t{node1.echoed_input} {op} {node2.echoed_input}\n"
            output_content += input_expression

            # Case when we add or subtract terms
            if op in ("+", "-"):

                # Distribute minus term to node2 data so we can add
                if op == "-":
                    for term, di in node2.data.items():
                        di["signed_coef"] *= -1

                # Add the terms
                simplified_expressions = add_expressions(node1, node2)

                simplified_expressions_str = concatenate_output_expressions(simplified_expressions)
                output_content += f"Output:\t{simplified_expressions_str}\n"

                print('here')

            print(f"After: {node2.data}")
        print("here")

        # index = 0
        # while index < evaluation_li.index:
        #    evaluation_set = evaluation_li.array[index]

        #    index += 1

        # node_c = polynomial_li.get_node("C")
        # node_d = polynomial_li.get_node("D")
        # d_c = node_c.data
        # d_d = node_d.data

        # d_cd_prod = multiply_expressions(node_c, node_d)

        # d_cd_sum = add_expressions(node_c, node_d)

        def evaluate():
            pass

        # Combine polynomial input
        # print(d_c)
        # print(d_d)
        # print(d_cd_prod)

        operation_message = "Polynomial simplification and evaluation"
        in_files = [polynomial_in_file, evaluation_in_file]
        with open(str(out_file), "w") as f:

            # Write header to file
            write_header(f, file_header, in_files, out_file, operation_message)
            f.write(output_content)
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
