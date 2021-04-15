"""Peter Rasmussen, Lab 3, __main__.py

This program recursively converts a file of newline-delimited prefix expressions into an output of
postfix expressions. Each line of the output begins with the line number of the prefix expression
from the input file, followed by the echoed prefix expression and its postfix equivalent. Postfix
expressions are not rendered for invalid prefix expressions (i.e., those that have syntax errors).
In these cases, the prefix syntax error is written instead of a postfix expression.

Header statements make up the first four lines of the output file. Prefix processing outputs are
listed line by line thereafter. Each line of prefix output begins with the line number of the
corresponding prefix expression. Then, the original prefix statement is echoed. Finally, the postfix
expression is written. Below the conversion outputs are complexity outputs: time and number of
loops, a crude proxy for space complexity.

Below the prefix-postfix outputs is a footer which provides a brief complexity summary. This summary
lists the number of lines, runtime (in nanoseconds), and runtime per line for the three key methods
used in this program: run (in run.py), PrefixPreprocessor.preprocess_prefix_input (in
parse_polynomial_input.py), and PrefixConverter.convert_prefix_to_postfix (in prefix_converter.py).
The prefix_converter method complexity summary also includes the total number of recursive calls
made. More details on these functions, including their definitions, are provided in each respective
module.

Example output file:

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Peter Rasmussen, Lab 3
    # Input file: /Users/peter/PycharmProjects/PRasmussenlab3/resources/additional_input.txt
    # Output file: /Users/peter/PycharmProjects/PRasmussenlab3/resources/additional_output.txt

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Prefix-postfix conversion
    Line 1: Prefix: Peter Rasmussen, Lab 3, Postfix: PrefixSyntaxError('Prefix statement cannot begin with an operand character')
    ...
    Line 14: Prefix: +$, Postfix: PrefixSyntaxError('Column 2: Too many operators, 2, for operand characters, 0.')

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    Complexity outputs
    run
        lines: 15
        elapsed_ns: 3136000
        lines_per_ns: 4.783163265306122e-06
    prefix_processor
        elapsed_ns: 1904000
        lines_per_ns: 7.878151260504201e-06
    prefix_converter
        elapsed_ns: 233000
        lines_per_ns: 6.437768240343348e-05
        n_recursive_calls: 17

Upon execution, the user must provide the input file path (in_file) and output file path (out_file).
Optionally, the user may specify whether to include numerals as acceptable operand symbols and
whether to include additional operators. Please note that only single-digit numerals (0-9) are
supported in this implementation. Additionally, the user may specify a file header that is
prepended to the outputs. Please refer to the arg_parser statements for more information on these
optional arguments.

Example execution:
    python -m path/to/lab3 -i path/to/input_file.txt -o path/to/output_file.txt

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
