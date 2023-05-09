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

    # Displays in console the different trees that can be used and their respective InOrder dlist ->
    #      ->  Will be removed prior to hand in.

    def test_newTree(self):
        """Testing the newTree generation: Displays in console"""
        test_tree = BinarySearchTree()
        # Display the two trees used for the test
        print("NewTree. 1")
        test_tree._root = self.newTree(1)
        test_tree.display()
        print("InOrder list:" + str(test_tree.inorder_list()))
        print("NewTree. 2")
        test_tree._root = self.newTree(2)
        test_tree.display()
        print("InOrder list:" + str(test_tree.inorder_list()))
        print("NewTree. 3")
        test_tree._root = self.newTree(3)
        test_tree.display()
        print("InOrder list:" + str(test_tree.inorder_list()))

    # Test for exercise 2
    """
    Use the inOrder list created by a method of bintree in order to create an ordered list of the elements 
    of the treeOut. 
    The assert-equal method can then compare the str form of this list with the expected str form after doing the
    operation. 
      """
    """
    def test1_test01(self):
        self.tree1._root = self.newTree(1)
        self.tree1.display()
        print(self.tree1.find_dist_k(13,2))
    """
    # MERGE: All elements. From tree1 and tree 2
    # When both trees are empty: Return empty tree
    def test2_test01(self):
        """E2: Merge, both empty"""
        self.opc = "Merge"
        self.tree1._root = None
        self.tree2._root = None

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)

        # Expect an empty list. Either one of the trees outputs an empty list with the inorder_list method
        expected = self.tree1.inorder_list()
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("TEST 1: Merge ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()
        print("-------------------")
        self.treeOut.display()

    # When only one tree is empty: Return only the other tree
    def test2_test02(self):
        """E2: Merge, one empty"""
        self.opc = "Merge"
        self.tree1._root = self.newTree(1)
        self.tree2._root = None

        self.treeOut= phase2.create_tree(self.tree1, self.tree2, self.opc)

        # Only the tree1 elements should be in the final tree
        expected = self.tree1.inorder_list()
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("TEST 2: Merge ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()
        print("-------------------")
        self.treeOut.display()

    # When both trees have elements
    def test2_test03(self):
        """E2: Merge, normal"""
        self.opc = "Merge"
        self.tree1._root = self.newTree(1)
        self.tree2._root = self.newTree(3)

        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        # Expect the str form of a list with all the elements of tree1 and tree2 ordered and without repetitions.
        expected = "[1, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 30, 49, 50, 55]"
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("TEST 3: Merge ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()
        print("-------------------")
        self.treeOut.display()

    # INTERSECT: Elements that are both in tree1 and tree 2

    # Intersect two emtpy trees: Return an empty tree
    def test2_test04(self):
        "E2: Intersect, both emtpy"
        self.opc = "Intersect"
        self.tree1._root = None
        self.tree2._root = None
        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        # Expect the str form of the inorder_list of any tree. Both will return an empty list
        expected = self.tree1.inorder_list()
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("TEST 4: Intersect ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()
        print("-------------------")
        self.treeOut.display()

    # Intersect one empty and one non-empty tree: Return emtpy tree
    def test2_test05(self):
        """E2: Intersect, one empty"""
        self.opc = "Intersect"
        self.tree1._root = self.newTree(1)
        self.tree2._root = None
        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        # Expect the str form of the tree2 InOrder_list. It will return an emtpy list
        expected = self.tree2.inorder_list()
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("TEST 5: Intersect ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()
        print("-------------------")
        self.treeOut.display()

    # Intersect two identical trees: Return same tree as any of the two inputs
    def test2_test06(self):
        """E2: Intersect, identical"""
        self.opc = "Intersect"
        self.tree1._root = self.newTree(1)
        self.tree2._root = self.newTree(1)
        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        # Expect the str created by the InOrder_list method from any of the trees.
        expected = self.tree2.inorder_list()
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("TEST 6: Intersect ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()
        print("-------------------")
        self.treeOut.display()

    # Intersect two trees with no elements in common: Return emtpy tree (root none)
    def test2_test07(self):
        """E2: Intersect, all different"""
        self.opc = "Intersect"
        self.tree1._root = self.newTree(1)
        self.tree2._root = self.newTree(2)
        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)
        # Expect the str form from any tree InOrder_list. It will return an emtpy list
        expected = "[]"
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("TEST 7: Intersect ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()
        print("-------------------")
        self.treeOut.display()

    # Intersect two trees with "any" elems: Return a tree with the elements repeated on both trees
    def test2_test08(self):
        """E2: Intersect, normal"""
        self.opc = "Intersect"
        self.tree1._root = self.newTree(1)
        self.tree2._root = self.newTree(3)
        self.treeOut = phase2.create_tree(self.tree1, self.tree2, self.opc)

        # Display the output tree
        print("TEST 8: Intersect ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()
        print("-------------------")
        self.treeOut.display()
        # The expected str form of a list is the one with all the elements repeated in both trees
        expected = "[5, 6, 9, 10, 20]"
        self.assertEqual(str(expected), str(self.treeOut.inorder_list()))

        # Display the output tree
        print("TEST 8: Intersect ")
        self.tree1.display()
        print("-------------------")
        self.tree2.display()
        print("-------------------")
        self.treeOut.display()

    # DIFFERENCE: Elems of tree1 that are not on tree2.
    """The difference is the same as an intersection of all elements that are in A but ARE NOT IN Bchckes if ."""

    # Difference: Normal case
    def test2_test09(self):
        """E2: Difference, normal"""

        phase2.create_tree(self.tree1, self.tree2, self.opc)


# Some usage examples
if __name__ == '__main__':
    unittest.main()
