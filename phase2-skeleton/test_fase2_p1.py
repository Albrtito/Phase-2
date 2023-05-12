# -*- coding: utf-8 -*-
"""
Test battery, using unittest, to figure out some metrics about student's code
@author: EDA Team
"""

# Classes provided by EDA Team
from bst import BinarySearchTree
from bintree import BinaryNode

# Test case support
import unittest

# Exercises implementation (the one used as reference, and the students one)
# Classes containing the different solutions

#from phase2_1_gsg import BST2
from phase2 import BST2


class Test(unittest.TestCase):
    # Provisional mark
    mark_exercise_01 = 0
    mark_exercise_02 = 0

    """
    def testz_print_mark(self):
        print(f"*************************")
        print(f"** Provisional mark E01 = {Test.mark_exercise_01}")
        print(f"** Provisional mark E02 = {Test.mark_exercise_02}")
        print(f"*************************")
    """
    def setUp(self):
        # Cases: E01.01 .. E01.07
        self.tree01_description = BST2()
        self.tree01_elements = [14, 11, 18, 10, 13, 16, 19, 5, 12, 15, 17, 30, 4, 6, 29, 31, 2, 8, 24, 33, 1, 3, 7, 9, 23, 25, 32, 34, 21, 27, 36, 20, 22, 26, 28, 35, 37]
        for x in self.tree01_elements:
            self.tree01_description.insert(x)
        # self.tree01_description.draw()
        # Cases: E01.08
        self.tree01_empty = BST2()
        # Cases: E01.09 .. E01.11
        self.tree01_size_1 = BST2()
        self.tree01_size_1.insert(1)

    def test_exercise01_test_01(self):
        print('Case E01.01: Exercise description. Test 01', end=" ")
        result = self.tree01_description.find_dist_k(30, 0)
        result.sort()
        self.assertTrue(result == [30])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_02(self):
        print('Case E01.02: Exercise description. Test 02', end=" ")
        result = self.tree01_description.find_dist_k(30, 2)
        result.sort()
        # print(result)
        # self.tree01_description.draw()
        self.assertTrue(result == [18, 24, 33])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_03(self):
        print('Case E01.03: Exercise description. Test 03', end=" ")
        result = self.tree01_description.find_dist_k(12, 6)
        result.sort()
        self.assertTrue(result == [2, 8, 15, 17, 30])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_04(self):
        print('Case E01.04: Exercise description. Test 04', end=" ")
        result = self.tree01_description.find_dist_k(17, 7)
        result.sort()
        self.assertTrue(result == [4, 6, 23, 25, 32, 34])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_05(self):
        print('Case E01.05: Exercise description. Test 05', end=" ")
        result = self.tree01_description.find_dist_k(26, 9)
        result.sort()
        self.assertTrue(result == [11, 15, 17, 36])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_06(self):
        print('Case E01.06: Exercise description. Test 05 + k = 1000', end=" ")
        result = self.tree01_description.find_dist_k(30, 1000)
        result.sort()
        self.assertTrue(result == [])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_07(self):
        print('Case E01.07: Exercise decription. Any number in the tree (no hardcoded!)', end=" ")
        result = self.tree01_description.find_dist_k(24, 3)
        result.sort()
        self.assertTrue(result == [19, 20, 22, 26, 28, 31])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_08(self):
        print('Case E01.08: emptyTree', end=" ")
        result = self.tree01_empty.find_dist_k(1, 1)
        result.sort()
        self.assertTrue(result == [])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_09(self):
        print('Case E01.09: tree.size = 1 and n = 2 (not in the tree) and any k', end=" ")
        result = self.tree01_size_1.find_dist_k(2, 1)
        result.sort()
        self.assertTrue(result == [])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_10(self):
        print('Case E01.10: tree.size = 1 and n=1 and tree.root.elem = 1 and k = 0', end=" ")
        result = self.tree01_size_1.find_dist_k(1, 0)
        result.sort()
        self.assertTrue(result == [1])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_11(self):
        print('Case E01.11: tree.size = 1 and n=1 and tree.root.elem = 1 and k = 1', end=" ")
        result = self.tree01_size_1.find_dist_k(1, 1)
        result.sort()
        self.assertTrue(result == [])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

# Some usage examples
if __name__ == '__main__':
    unittest.main()
