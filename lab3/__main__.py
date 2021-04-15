"""Peter Rasmussen, Lab 3, __main__.py

This program ingests polynomial expressions and performs addition, multiplication, and subtraction
operations on those expressions. A variable-values dataset is used to evaluate the expressions
across a range of values.

Header statements make up the first seven lines of the output file. Polynomial operation and
evaluation outputs are listed thereafter. Polynomials A, B, C, and D are defined underneath the
header. Below the polynomial definitions, the outputs of the operations and evaluations are
provided.

Outputs are organized by operation (e.g., A+B). For each operation, the input polynomial expression
is echoed and the output expression (e.g., result of A+B) is one line below. A simple table
summarizes the evaluated answer alongside the evaluation set (e.g., x1y2z3). Below the polynomial
expression operation and evaluation outputs is total runtime.

Example output file:

    # Peter Rasmussen, Lab 3
    # Polynomial simplification and evaluation
    # Input files:
    #	/Users/peter/PycharmProjects/PRasmussenLab3/resources/additional_polynomial_input_04.txt
    #	/Users/peter/PycharmProjects/PRasmussenLab3/resources/additional_evaluation_input_02.txt
    # Output file: /Users/peter/PycharmProjects/PRasmussenLab3/resources/additional_output_04_02.txt

    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    Polynomial input expression definitions
    A = 31a3b4c3d4e1+11a4b1c0d0e0-1a4b1c3d3e3-13a2b3c2d4e0+24a1b3c4d4e3
    B = 7a1b4c2d3e1-29a1b2c3d0e2-25a3b2c0d4e3+6a4b2c0d1e2-1a1b0c2d0e3
    C = a2b1c3d1e1-10a2b1c0d3e4+23a4b2c2d3e2+16a0b2c2d3e2-5a2b1c1d1e2
    D = 4a3b1c0d1e2+24a4b4c2d0e2+28a2b3c2d1e0+18a1b3c0d2e1-16a1b4c4d0e2
    A+B
    Input:	(31a3b4c3d4e1+11a4b1c0d0e0-1a4b1c3d3e3-13a2b3c2d4e0+24a1b3c4d4e3)+(7a1b4c2d3e1-29a1b2c3d0e2-25a3b2c0d4e3+6a4b2c0d1e2-1a1b0c2d0e3)
    Output:	31a3b4c3d4e1+11a4b1c0d0e0-1a4b1c3d3e3-13a2b3c2d4e0+24a1b3c4d4e3+7a1b4c2d3e1-29a1b2c3d0e2-25a3b2c0d4e3+6a4b2c0d1e2-1a1b0c2d0e3
    Evaluation Set			Answer
    a0b4c1d5e4				0
    a2b3c5d0e1				-64772

Upon execution, the user must provide the polynomial input file path (polynomial_in_file),
evaluation input file path (evaluation_in_file), and output file path (out_file). Optionally, the
user may specify whether to modify the default header and whether to run the tests module.

Example execution:
    python -m path/to/lab3 -p path/to/poly_file.txt -e path/to/eval_file.txt

The structure of this package is based on the Python lab0 package that Scott Almes developed for
this course. Per Scott Almes, this module "is the entry point into this program when the module is
executed as a standalone program."

"""

# standard library imports
import argparse
from pathlib import Path

# local imports
from lab3.run import run


# Parse arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument(
    "--evaluation_in_file", "-e", type=Path, help="Evaluation input file path"
)
arg_parser.add_argument(
    "--polynomial_in_file", "-p", type=Path, help="Polynomial input file path"
)
arg_parser.add_argument("--out_file", "-o", type=Path, help="Output file path")
arg_parser.add_argument(
    "--file_header",
    "-f",
    default="Peter Rasmussen, Lab 3",
    type=str,
    help="Specify file header",
)
arg_parser.add_argument(
    "--test", "-t", type=bool, default=False, help="True to run tests"
)
args = arg_parser.parse_args()

# Execute prefix-to-postfix conversion run function
run(
    args.evaluation_in_file,
    args.polynomial_in_file,
    args.out_file,
    args.file_header,
    args.test,
)
