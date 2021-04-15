"""Peter Rasmussen, Lab 3, run.py

This module processes a polynomial expressions file and a corresponding variable-value evaluation
file to symbolically combine and then evaluate polynomial expressions.

"""

# standard library imports
from pathlib import Path
from time import time_ns

# local imports
from lab3.file_io import make_input_polynomial_string, make_header
from lab3.parsers.parse_polynomial_input import parse_polynomial_input
from lab3.parsers.parse_evaluation_input import parse_evaluation_input
from lab3.polynomial_operations import polynomial_operations
from lab3.evaluators.combine import (
    add_expressions,
    concatenate_output_expressions,
    multiply_expressions,
)
from lab3.symbols import Symbols
from lab3.tests import tests
from lab3.utils import remove_cruft


def run(
    evaluation_in_file: Path,
    polynomial_in_file: Path,
    out_file: Path,
    file_header: str,
    test: bool,
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
        in_files = [polynomial_in_file, evaluation_in_file]
        operation_message = "Polynomial simplification and evaluation"
        output_content = make_header(file_header, in_files, out_file, operation_message)

        # Read and parse polynomial input
        polynomial_li = parse_polynomial_input(polynomial_in_file)

        # Read and parse evaluation input
        evaluation_li = parse_evaluation_input(evaluation_in_file)

        # Write each input polynomial expression
        output_content += make_input_polynomial_string(polynomial_li, symbols)

        # For each set of evaluation inputs, evaluate polynomials
        for polynomial_operation in polynomial_operations:

            # Extract node data from polynomial list
            node_label1, op, node_label2 = polynomial_operation
            node1 = polynomial_li.get_node(node_label1)
            node2 = polynomial_li.get_node(node_label2)
            node_d1, node_d2 = node1.data, node2.data

            # Echo operation (e.g., A + B)
            output_content += f"{polynomial_operation}\n"

            # Echo polynomial expression input
            lhs = remove_cruft(node1.echoed_input)
            rhs = remove_cruft(node2.echoed_input)
            input_expression = f"Input:\t({lhs}){op}({rhs})\n"
            output_content += input_expression

            # Verify operator is supported by this implementation
            if op not in ("+", "-", "*"):

                # Raise error if a non-supported operator provided
                output_content += f"Output:\tOperator {op} is not supported."

            # Otherwise, process terms
            else:
                # Case when we add or subtract terms
                if op in ("+", "-"):

                    # Add the terms
                    simplified_expressions = add_expressions(node_d1, node_d2, op)

                # Case when we multiply terms
                else:
                    simplified_expressions = multiply_expressions(node_d1, node_d2)

                # Build simplified expressions output string
                simplified_expressions_str = concatenate_output_expressions(
                    simplified_expressions
                )
                output_content += f"Output:\t{simplified_expressions_str}\n"

                # Evaluate expressions for each variable-value set
                eval_li_index = 0
                output_content += "Evaluation Set\t\t\tAnswer\n"
                while eval_li_index < evaluation_li.index:
                    evaluation_set = evaluation_li.array[eval_li_index]
                    echoed_input = evaluation_set.echoed_input
                    tabs = "\t" * max(0, (5 - int(len(echoed_input) / 8)))

                    # Evaluate polynomial expression
                    expression_val = 0
                    for term, di in simplified_expressions.items():
                        term_val = 1
                        for var_ix, var in enumerate(evaluation_set.variables):
                            if var:
                                term_pow_ix = 2 * var_ix + 1
                                var_val = evaluation_set.get_node(var).signed_value
                                pow_val = int(term[term_pow_ix])
                                var_to_the_pow = var_val ** pow_val
                                term_val *= var_to_the_pow
                        expression_val += di["signed_coef"] * term_val

                    output_content += f"{echoed_input}{tabs}{expression_val}\n"

                    eval_li_index += 1

                # Skip a line between expression evaluations
                output_content += "\n"

        run_stop = time_ns()
        run_elapsed = run_stop - run_start

        output_content += "\n"
        output_content += f"Runtime: {run_elapsed}"

        # Write outputs to file
        with open(str(out_file), "w") as f:

            # Write header to file
            f.write(output_content)
