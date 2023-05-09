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

"""
Comments: 
With respect to the usage of list: The function _inorder_list used,
as well as the other traverse to list functions, normal python list. 
Because this phase does not allow the usage of python list the inorder_list 
and it´s aux function have been altered to work with dlist. The other 
traverse to list functions still work using python list but are not used 
for this phase´s code. 
"""


class Test(unittest.TestCase):
    def setUp(self):
        # A binary search tree: exercise 1 test
        self.bst2 = BST2()

        # Two binary trees: Exercise 2
        self.tree1 = BinarySearchTree()
        self.tree2 = BinarySearchTree()
        # Output tree : Exercise 2
        self.treeOut = BinarySearchTree()
        # The variable for deciding type of operation between trees
        self.opc = None

    def newTree(self, option: int):
        """This function can create one of three possible trees: Created manually. Creation by
        returning the root."""
        root = None
        if option == 1:
            root = BinaryNode(10)
            # Left side
            root.left = BinaryNode(8)
            root.left.left = BinaryNode(5)
            root.left.left.left = BinaryNode(1)
            root.left.left.right = BinaryNode(6)
            root.left.right = BinaryNode(9)
            # Right side
            root.right = BinaryNode(13)
            root.right.left = BinaryNode(11)
            root.right.left.right = BinaryNode(12)
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
        elif option == 3:  # This tree has no elements in common with the option 1
            root = BinaryNode(14)
            # Left side
            root.left = BinaryNode(9)
            root.left.left = BinaryNode(5)
            root.left.left.left = BinaryNode(4)
            root.left.left.right = BinaryNode(6)
            root.left.right = BinaryNode(10)
            # Right side
            root.right = BinaryNode(50)
            root.right.left = BinaryNode(30)
            root.right.left.left = BinaryNode(21)
            root.right.left.left.left = BinaryNode(20)
            root.right.left.left.left.left = BinaryNode(15)
            root.right.left.right = BinaryNode(49)
            root.right.right = BinaryNode(55)
            return root

    # Test for exercise 2
    """
    Use the inOrder list created by a method of bintree in order to create an ordered list of the elements 
    of the treeOut. 
    The assert-equal method can then compare the str form of this list with the expected str form after doing the
    operation. 
      """

    # MERGE: All elements. From tree1 and tree 2
    # When both trees are empty: Return empty tree
    def test2_test01(self):
        """E2: Merge, both empty"""
        self.opc = "Merge"
        self.tree1._root = None
        self.tree2._root = None

        # Print the test number. Case. And the two trees in the operation
        print("TEST 1: Merge both empty ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()

        # Expect an empty list. Either one of the trees outputs an empty list with the inorder_list method
        expected = self.tree1.inorder_list()

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("-------------------")
        self.treeOut.display()

    # When only one tree is empty: Return only the other tree
    def test2_test02(self):
        """E2: Merge, one empty"""
        self.opc = "Merge"
        self.tree1._root = self.newTree(1)
        self.tree2._root = None

        # Print the test number. Case. And the two trees in the operation
        print("TEST 2: Merge one emtpy ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()

        # Only the tree1 elements should be in the final tree
        expected = self.tree1.inorder_list()

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("-------------------")
        self.treeOut.display()

    # When both trees have elements
    def test2_test03(self):
        """E2: Merge, normal"""
        self.opc = "Merge"
        self.tree1._root = self.newTree(1)
        self.tree2._root = self.newTree(3)

        # Print the test number. Case. And the two trees in the operation
        print("TEST 3: Merge normal ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()

        # Expect the str form of a list with all the elements of tree1 and tree2 ordered and without repetitions.
        expected = "[1, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 30, 49, 50, 55]"

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("-------------------")
        self.treeOut.display()

    # INTERSECT: Elements that are both in tree1 and tree 2

    # Intersect two emtpy trees: Return an empty tree
    def test2_test04(self):
        "E2: Intersect, both emtpy"
        self.opc = "Intersect"
        self.tree1._root = None
        self.tree2._root = None

        # Print the test number. Case. And the two trees in the operation
        print("TEST 4: Intersect both empty ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()

        # Expect the str form of the inorder_list of any tree. Both will return an empty list
        expected = self.tree1.inorder_list()

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("-------------------")
        self.treeOut.display()

    # Intersect one empty and one non-empty tree: Return emtpy tree
    def test2_test05(self):
        """E2: Intersect, one empty"""
        self.opc = "Intersect"
        self.tree1._root = self.newTree(1)
        self.tree2._root = None

        # Print the test number. Case. And the two trees in the operation
        print("TEST 5: Intersect one empty ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()

        # Expect the str form of the tree2 InOrder_list. It will return an emtpy list
        expected = self.tree2.inorder_list()

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("-------------------")
        self.treeOut.display()

    # Intersect two identical trees: Return same tree as any of the two inputs
    def test2_test06(self):
        """E2: Intersect, identical"""
        self.opc = "Intersect"
        self.tree1._root = self.newTree(1)
        self.tree2._root = self.newTree(1)

        # Print the test number. Case. And the two trees in the operation
        print("TEST 6: Intersect identical ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()

        # Expect the str created by the InOrder_list method from any of the trees.
        expected = self.tree2.inorder_list()

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("-------------------")
        self.treeOut.display()

    # Intersect two trees with no elements in common: Return emtpy tree (root none)
    def test2_test07(self):
        """E2: Intersect, all different"""
        self.opc = "Intersect"
        self.tree1._root = self.newTree(1)
        self.tree2._root = self.newTree(2)

        # Print the test number. Case. And the two trees in the operation
        print("TEST 7: Intersect all different ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()

        # Expect the str form from any tree InOrder_list. It will return an emtpy list
        expected = "[]"

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("-------------------")
        self.treeOut.display()

    # Intersect two trees with "any" elems: Return a tree with the elements repeated on both trees
    def test2_test08(self):
        """E2: Intersect, normal"""
        self.opc = "Intersect"
        self.tree1._root = self.newTree(1)
        self.tree2._root = self.newTree(3)

        # Print the test number. Case. And the two trees in the operation
        print("TEST 8: Intersect normal ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()

        # The expected str form of a list is the one with all the elements repeated in both trees
        expected = "[5, 6, 9, 10, 20]"

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("-------------------")
        self.treeOut.display()

    # DIFFERENCE: Elems of tree1 that are not on tree2.

    # Difference: Both empty. Return empty tree
    def test2_test09(self):
        """E2: Difference, both empty"""
        self.opc = "Difference"
        self.tree1._root = None
        self.tree2._root = None

        # Print the test number. Case. And the two trees in the operation
        print("TEST 9: Difference both empty ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()

        # Expect to return an empty tree -> An empty Dlist
        expected = "[]"

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("-------------------")
        self.treeOut.display()

    # Difference: First one empty. Return emtpy tree. No elements in common -> Nothing to remove
    def test2_test010(self):
        """E2: Difference, first empty"""
        self.opc = "Difference"
        self.tree1._root = None
        self.tree2._root = self.newTree(3)

        # Print the test number. Case. And the two trees in the operation
        print("TEST 10: Difference first emtpy ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()

        # Expect an empty tree. Then the list is emtpy
        expected = "[]"

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree

        print("-------------------")
        self.treeOut.display()

    # Difference: Second one emtpy. Return the first one. Nothing to remove, nothing in common
    def test2_test011(self):
        """E2: Difference, second emtpy"""
        self.opc = "Difference"
        self.tree1._root = self.newTree(1)
        self.tree2._root = None

        # Expect the string form of a list with the ordered elements of tree1
        expected = str(self.tree1.inorder_list())

        # Print the test number. Case. And the two trees in the operation
        print("TEST 11: Difference second empty ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("-------------------")
        self.treeOut.display()

    # Difference: Normal case
    def test2_test12(self):
        """E2: Difference, normal"""
        self.opc = "Difference"
        self.tree1._root = self.newTree(1)
        print("TEST 12: Difference normal ")
        self.tree1.display()
        self.tree2._root = self.newTree(3)

        # Expect the string form of a list with the proper elements corresponding to the difference
        expected = "[1, 8, 11, 12, 13]"

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("-------------------")
        self.tree2.display()
        print("-------------------")
        self.treeOut.display()

        phase2.create_tree(self.tree1, self.tree2, self.opc)


# Some usage examples
if __name__ == '__main__':
    unittest.main()
