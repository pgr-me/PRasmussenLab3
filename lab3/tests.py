"""Peter Rasmussen, Lab 3, __main__.py

This program tests selected modules, including  polynomial_list, polynomial_syntax_checker, and
make_polynomial_list. Run this module in the PRasmussenLab3/lab3 directory.

"""


# Standard library imports
import argparse

# Local imports
from node import Node


def test_polynomial_list():
    """Test polynomial_list module."""
    from polynomial_list import PolynomialList
    print("")
    print(80 * "@")
    print("polynomial_list tests:")
    print("Test insert and traverse methods:")
    passed = True
    try:
        li = PolynomialList()
        node_a = Node('A', 1)
        node_b = Node('B', 2)
        node_x = Node('X', 2)
        node_c = Node('C', 4)
        li.insert(node_a, direction='right')
        li.insert(node_b, direction='right')
        li.insert(node_x, direction='left')
        li.insert(node_c, direction='right')
        li.traverse(data=True)
        print("\tPassed")
    except Exception as e:
        print(f"\tFailed: {e}")
        passed = False

    print("")
    print("Test merge_nodes method:")
    if passed:
        try:
            def add_them(node_left, node_right):
                return node_left.data + node_right.data
            li.merge_nodes("A", "B", add_them)
            li.traverse(data=True)
            print("\tPassed")

        except Exception as e:
            print(f"\tFailed: {e}")
    else:
        print("\tCould not test merge_nodes method because of prior error with insert / traverse"
              "methods")


def test_polynomial_syntax_checker():
    """Test polynomial syntax checker module."""
    from polynomial_syntax_checker import PolynomialSyntaxChecker, PolynomialSyntaxError
    print(f"\n{80 * '@'}\npolynomial_syntax_checker tests:")
    passed = True
    psc = PolynomialSyntaxChecker()

    print("\nTest check_if_leading_zero method:")
    try:
        psc.check_if_leading_zero("054", column=1)
        print("\tPassed")
    except PolynomialSyntaxError:
        passed = True
        print("\tFailed")

    print("\nTest check_if_legal_symbol method:")
    if passed:
        try:
            psc.check_if_legal_symbol("$A+0", column=1)
            print("\tPassed")
        except PolynomialSyntaxError:
            print("\tFailed")


def test_make_polynomial_list():
    #from make_polynomial_list import MakePolynomialList
    pass

def main():
    test_polynomial_list()
    test_polynomial_syntax_checker()
    test_make_polynomial_list()

if __name__ == "__main__":
    main()