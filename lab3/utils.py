"""Peter Rasmussen, Lab 3, utils.py

This module provides miscellaneous utility functions used by other modules.

"""

# standard library imports
from io import TextIOWrapper
import os
from pathlib import Path, PosixPath, PurePath, PurePosixPath, PureWindowsPath, WindowsPath
from time import time_ns
from typing import Union


class Timer:
    """Measure elapsed time."""
    def __init__(self):
        self.start: int = time_ns()
        self.stop: Union[int, None] = None
        self.elapsed: Union[int, None] = None

    def stop_timer(self) -> int:
        """
        Stop timer and compute elapsed time.
        :return: Elapsed time
        """
        self.stop = time_ns()
        self.elapsed = self.stop - self.start
        return self.elapsed


def array_to_string(a: list) -> str:
    """
    Convert an array to a string.
    :param a: List of elements
    :return: String of concatenated elements
    """
    s = ""
    for i in a:
        s += i
    return s


def copy_list(in_li: list)->list:
    """
    Make a deep copy of a list.
    :param in_li: Input list
    :return: Deep copy of output list
    """
    out_li = []
    for i in in_li:
        out_li.append(i)
    return out_li


def header_helper(paths, kind="Input"):
    """
    Build file IO identification portion of header.
    :param paths: String, Path, list of paths, or tuple of paths
    :param kind: Input or Output
    :return: File IO identification message
    """
    # Check type for kind
    if kind not in ["Input", "Output"]:
        raise ValueError(f"Kind must be either 'Input' or 'Output'. You provided kind={kind}")

    # Build the path identification portion of header
    if type(paths) in [str, Path, PosixPath, PurePath, PurePosixPath, PureWindowsPath, WindowsPath]:
        file_msg = f"{kind} file: {paths.absolute()}\n"

    elif type(paths) in [list, tuple]:
        file_msg = f"{kind} files:\n"
        for path in paths:
            file_msg += f"#\t{path.absolute()}\n"

    # Raise an error if paths is of wrong type
    else:
        msg = f"{kind} must by of type str, Path, list, or tuple. You supplied {type(paths)}"
        raise TypeError(msg)

    return file_msg


def write_footer(file: TextIOWrapper, footer_di: dict):
    """
    Write the footer of a prefix-to-postfix conversion file.
    :param file: File-like object to write to
    :param footer_di: Dictionary of function names & their performance metrics and associated values
    """
    footer_str = ""
    for function_name, metric_di in footer_di.items():
        footer_str += function_name + os.linesep
        for metric, value in metric_di.items():
            footer_str += f"\t{metric}: {value}" + os.linesep
    file.write(os.linesep + f"# {98 * '@'}" + os.linesep)
    file.write("Complexity outputs" + os.linesep)
    file.write(footer_str)


def write_header(file: TextIOWrapper, header: str, in_paths, out_paths, operation_message):
    """
    Write the header of a prefix-to-postfix conversion file.
    :param file: File-like object to write to
    :param header: Single-line header string
    :param in_paths: Path to input file
    :param out_paths: Path to output file
    :param operation_message: Indicate what the program does
    """
    in_path_msg = header_helper(in_paths, "Input")
    out_path_msg = header_helper(out_paths, "Output")

    header = (
        f"# {98 * '@'}\n"
        f"# {header}\n"
        f"# {in_path_msg}"
        f"# {out_path_msg}"
        "\n"
    )
    file.write(header)
    file.write(f"# {98 * '@'}" + os.linesep)
    file.write(f"# {operation_message}" + os.linesep)
