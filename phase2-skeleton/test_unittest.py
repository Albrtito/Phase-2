# -*- coding: utf-8 -*-
"""
Test program comparing solutions with the builtin list-based one.

@author: EDA Team
"""

# Classes provided by EDA Team
from bst import BinarySearchTree
import unittest
from phase2 import BST2
from bintree import BinaryNode
import phase2
import random


class Test(unittest.TestCase):
    def setUp(self):
        # A binary search tree: exercise 1 test
        self.bst2 = BST2()

        # Two binary trees: Exercise 2
        self.tree1 = BST2()
        self.tree2 = BST2()
        # The variable for deciding type of operation between trees
        self.opc = None

    # Function created in order to create test trees more easily.
    def newTree(self, option: int):
        """This function can create one of four trees: Created manually. Creation by
        returning the root."""
        root = None
        if option == 1:
            root = BinaryNode(8)
            root.left = BinaryNode(5)
            root.left.left = BinaryNode(4)
            root.left.left.left = BinaryNode(1)
            root.left.left.right = BinaryNode(6)
            root.left.right = BinaryNode(7)
            root.right = BinaryNode(13)
            root.right.left = BinaryNode(10)
            root.right.left.left = BinaryNode(9)
            root.right.left.right = BinaryNode(11)
            root.right.right = BinaryNode(20)
            return root
        elif option == 2:  # This tree has no elements in common with the option 1
            root = BinaryNode(40)
            # Left side
            root.left = BinaryNode(35)
            root.left.left = BinaryNode(30)
            root.left.left.left = BinaryNode(21)
            root.left.left.right = BinaryNode(31)
            root.left.right = BinaryNode(37)
            # Right side
            root.right = BinaryNode(50)
            root.right.left = BinaryNode(48)
            root.right.left.left = BinaryNode(45)
            root.right.left.right = BinaryNode(49)
            root.right.right = BinaryNode(55)
            return root
        elif option == 3:
            root = BinaryNode(8)
            root.left = BinaryNode(5)
            root.left.left = BinaryNode(4)
            root.left.left.left = BinaryNode(1)
            root.left.left.right = BinaryNode(6)
            root.left.right = BinaryNode(7)
            root.right = BinaryNode(13)
            root.right.left = BinaryNode(10)
            root.right.left.left = BinaryNode(9)
            root.right.left.right = BinaryNode(11)
            root.right.right = BinaryNode(20)
            return root
        else:
            root = BinaryNode(8)
            root.left = BinaryNode(5)
            root.left.left = BinaryNode(4)
            root.left.left.left = BinaryNode(1)
            root.left.left.right = BinaryNode(6)
            root.left.right = BinaryNode(7)
            root.right = BinaryNode(13)
            root.right.left = BinaryNode(10)
            root.right.left.left = BinaryNode(9)
            root.right.left.right = BinaryNode(11)
            root.right.right = BinaryNode(20)
            return root

    def test_newTree(self):
        """Testing the newTree generation"""
        test_tree = BST2()
        # Display first possible tree creation
        print("NewTree. 1")
        test_tree._root = self.newTree(1)
        test_tree.display()
        print("NewTree. 2")
        test_tree._root = self.newTree(2)
        test_tree.display()
        print("NewTree. 3")
        test_tree._root = self.newTree(3)
        test_tree.display()
        print("NewTree. 4")
        test_tree._root = self.newTree(4)
        test_tree.display()

    # Test for exercise 2

    # MERGE: All elements. From tree1 and tree 2

    # When both trees are empty: Return empty tree
    def test2_test01(self):
        """E2: Merge, both empty"""
        self.opc = "Merge"
        self.tree1._root = None
        self.tree2._root = None

        phase2.create_tree(self.tree1, self.tree2, self.opc)

    # When only one tree is empty: Return only the other tree
    def test2_test02(self):
        """E2: Merge, one empty"""
        self.opc = "Merge"
        self.tree1._root = self.newTree(1)
        self.tree2._root = None

        phase2.create_tree(self.tree1, self.tree2, self.opc)

    # When both trees have elements
    def test2_test03(self):
        """E2: Merge, normal"""
        self.opc = "Merge"
        self.tree1._root = self.newTree(2)
        self.tree2._root = self.newTree(3)

        phase2.create_tree(self.tree1, self.tree2, self.opc)

    # INTERSECT: Elements that are both in tree1 and tree 2

    # Intersect two emtpy trees: Return an empty tree
    def test2_test04(self):
        "E2: Intersect, both emtpy"
        self.tree1._root = None
        self.tree2._root = None
        phase2.create_tree(self.tree1, self.tree2, self.opc)

    # Intersect one empty and one non-empty tree: Return emtpy tree
    def test2_test05(self):
        """E2: Intersect, one empty"""
        self.tree1._root = self.newTree(4)
        self.tree2._root = None
        phase2.create_tree(self.tree1, self.tree2, self.opc)

    # Intersect two ideltical trees: Return same tree as any of the two inputs
    def test2_test06(self):
        """E2: Intersect, identical"""
        tree_creation_option = random.randint(1, 4)
        self.tree1._root = self.newTree(tree_creation_option)
        self.tree2._root = self.newTree(tree_creation_option)
        phase2.create_tree(self.tree1, self.tree2, self.opc)

    # Intersect two trees with no elements in common: Return emtpy tree (root none)
    def test2_test07(self):
        """E2: Intersect, different"""

        phase2.create_tree(self.tree1, self.tree2, self.opc)

    # Intersect two trees with "any" elems: Return the different elems between both trees.
    def test2_test08(self):
        """E2: Intersect, normal"""

        phase2.create_tree(self.tree1, self.tree2, self.opc)

    # DIFFERENCE: Elems of tree1 that are not on tree2.
    """The difference is the same as an intersection of all elements that are in A but ARE NOT IN Bchckes if ."""

    # Difference: Normal case
    def test2_test09(self):
        """E2: Difference, normal"""

        phase2.create_tree(self.tree1, self.tree2, self.opc)


# Some usage examples
if __name__ == '__main__':
    unittest.main()
