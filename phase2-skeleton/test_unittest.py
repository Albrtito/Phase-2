# -*- coding: utf-8 -*-
"""
Test program comparing solutions with the builtin list-based one.

@author: EDA Team
"""

# Classes provided by EDA Team
from bst import BinarySearchTree
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        ...

    # Test for exercise 2

    # MERGE: All elements. From tree1 and tree 2

    # When both trees are empty: Return empty tree
    def test2_test01(self):
        "E2: Merge, both empty"

    # When only one tree is empty: Return only the other tree
    def test2_test02(self):
        "E2: Merge, one empty"

    # When both trees have elements
    def test2_test03(self):
        "E2: Merge, normal"

    # INTERSECT: Elements that are both in tree1 and tree 2

    # Intersect two emtpy trees: Return an empty tree
    def test2_test04(self):
        "E2: Intersect, both emtpy"

    # Intersect one empty and one non-empty tree: Return emtpy tree
    def test2_test05(self):
        "E2: Intersect, one empty"

    # Intersect two ideltical trees: Return same tree as any of the two inputs
    def test2_test06(self):
        "E2: Intersect, identical"

    # Intersect two trees with no elements in common: Return emtpy tree (root none)
    def test2_test07(self):
        "E2: Intersect, identical"

    # Intersect two trees with "any" elems: Return the different elems between both trees.
    def test2_test08(self):
        "E2: Intersect, normal"




    #DIFFERENCE: Elems of tree1 that are not on tree2.
    """The difference is the same as an intersection of all elements that are in A but ARE NOT IN Bchckes if ."""

    # Difference: Normal case
    def test2_test09(self):
        "E2: Difference, normal"

# Some usage examples
if __name__ == '__main__':
    unittest.main()
