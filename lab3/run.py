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
from lab3.utils import Symbols
#from lab3.make_polynomial_list import MakeCircularList
#from lab3.prefix_converter import PrefixConverter
#from lab3.utils import array_to_string, write_footer, write_header


def run(
    in_file: Path,
    out_file: Path,
    file_header: str,
    test: bool
):
    """
    Convert a file of prefix statements to a file of prefix outputs which include complexity stats.
    :param in_file: Input file to read
    :param out_file: Output file to write to
    :param file_header: Header to add at top of output file
    :param use_numerals: True to include numerals among accepted_symbols
    :param additional_operators: String to include additional operators; otherwise None
    """

    #run_start = time_ns()

    ## Instantiate symbols object, which contains operands, operators, and other accepted characters
    #symbols = Symbols(
    #    use_numerals=use_numerals, additional_operators=additional_operators
    #)

    ## Preprocess prefix file, checking for errors and recording complexity metrics
    #prefix_preprocessor = MakeCircularList(
    #    in_file, symbols.operands, symbols.operators
    #)
    #file_di: dict = prefix_preprocessor.preprocess_prefix_input()
    #with open(str(out_file), "w") as f:

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
    if test:
        from lab3 import tests
        tests.main()