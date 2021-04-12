"""Peter Rasmussen, Lab 3, __main__.py

This program tests selected modules, including singly_linked_list, circular_list,
and polynomial_syntax_checker.

Run this module in the PRasmussenLab3/lab3 directory.

"""


# Local imports
from lab3.nodes import PolynomialNode, SimpleNode


def test_singly_linked_list():
    """Test singly_linked_list module."""
    from lab3.singly_linked_list import SinglyLinkedList

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


def test_circular_list():
    """Test circular_list module."""
    from lab3.circular_list import CircularList
    print(f"\n{80 * '@'}\ncircular_list tests:")
    print("Test insert and traverse methods:")
    try:
        li = CircularList()
        node_a = PolynomialNode('A', datatype=int)
        node_b = PolynomialNode('B', datatype=int)
        node_c = PolynomialNode('C', datatype=int)
        node_a.set_data(1)
        node_b.set_data(2)
        node_c.set_data(3)
        li.insert(node_a, direction='right')
        li.insert(node_b, direction='right')
        li.insert(node_c, direction='right')
        li.traverse(data=True)
        print("\tPassed")
    except Exception as e:
        print(f"\tFailed: {e}")


def test_polynomial_syntax_checker():
    """Test polynomial syntax checker module."""
    from lab3.polynomial_syntax_checker import PolynomialSyntaxChecker, PolynomialSyntaxError
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


def main():
    """Run each test."""
    test_singly_linked_list()
    test_circular_list()
    test_polynomial_syntax_checker()


if __name__ == "__main__":
    main()
