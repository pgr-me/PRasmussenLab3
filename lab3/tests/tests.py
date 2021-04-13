"""Peter Rasmussen, Lab 3, __main__.py

This program tests selected modules, including singly_linked_list, circular_list,
and polynomial_syntax_checker.

Run this module in the PRasmussenLab3/lab3 directory.

"""


# Standard library imports
from pathlib import Path

# Local imports
from lab3.nodes.polynomial_node import PolynomialNode
from lab3.nodes.simple_node import SimpleNode


def test_singly_linked_list():
    """Test singly_linked_list module."""
    from lab3.lists.singly_linked_list import SinglyLinkedList

    print(f"\n{80 * '@'}\nsingly_linked_list tests:")
    print("Test add_nodes method:")
    try:
        passed = True
        node_a = SimpleNode('A')
        node_b = SimpleNode('B')
        node_c = SimpleNode('C')
        node_d = SimpleNode('D')

        linked_list = SinglyLinkedList()
        linked_list.add(node_a)
        linked_list.add(node_b)
        linked_list.add(node_c)
        linked_list.add(node_d)
    except Exception as e:
        print(f"\tFailed: {e}")
        passed = False

    print("Test display and reverse methods:")
    if passed:
        try:
            print('Original list')
            linked_list.display()
            print(40 * '@')
            print('Reversed list')
            linked_list.reverse()
            linked_list.display()
        except Exception as e:
            print(f"\tFailed: {e}")


def test_polynomial_list():
    """Test polynomial_list module."""
    from lab3.lists.polynomial_list import PolynomialList
    print(f"\n{80 * '@'}\npolynomial_list tests:")
    print("Test insert and traverse methods:")
    try:
        li = PolynomialList()
        node_a = PolynomialNode()
        node_b = PolynomialNode()
        node_c = PolynomialNode()
        node_d = PolynomialNode()
        li.insert(node_a, direction='right')
        li.insert(node_b, direction='right')
        li.insert(node_c, direction='right')
        li.insert(node_d, direction='right')
        li.traverse(data=True)
        print("\tPassed")
    except Exception as e:
        print(f"\tFailed: {e}")


def test_make_polynomial_list():
    from lab3.parsers.parse_polynomial_input import parse_polynomial_input
    print(f"\n{80 * '@'}\nmake_polynomial_list tests:")
    print("Test required polynomial input:")
    in_file = Path("tests") / "test_make_polynomial_list_input.txt"
    li = parse_polynomial_input(in_file)
    li.traverse(data=True)


def test_parse_evaluation_input():
    from lab3.parsers.parse_evaluation_input import parse_evaluation_input
    evaluation_in_file = Path("tests") / "test_parse_evaluation_input.txt"
    eval_li = parse_evaluation_input(evaluation_in_file)
    index = 0
    while index <= eval_li.index - 1:
        var_val_li = eval_li.array[index]
        print(f'Variable: Value Set: {var_val_li.name}')
        for var in var_val_li.variables:
            node = var_val_li.get_node(var)
            print(f'\tVariable {var} = {node.value}')

        index += 1

def test_combine_terms():
    pass

def test_evaluate_terms():
    pass



#def test_polynomial_syntax_checker():
#    """Test polynomial syntax checker module."""
#    from lab3.polynomial_syntax_checker import PolynomialSyntaxChecker, PolynomialSyntaxError
#    print(f"\n{80 * '@'}\npolynomial_syntax_checker tests:")
#    passed = True
#    psc = PolynomialSyntaxChecker()
#
#    print("\nTest check_if_leading_zero method:")
#    try:
#        psc.check_if_leading_zero("054", column=1)
#        print("\tPassed")
#    except PolynomialSyntaxError:
#        passed = True
#        print("\tFailed")
#
#    print("\nTest check_if_legal_symbol method:")
#    if passed:
#        try:
#            psc.check_if_legal_symbol("$A+0", column=1)
#            print("\tPassed")
#        except PolynomialSyntaxError:
#            print("\tFailed")


def main():
    """Run each test."""
    test_singly_linked_list()
    test_polynomial_list()
    test_make_polynomial_list()
    test_parse_evaluation_input()


if __name__ == "__main__":
    main()
