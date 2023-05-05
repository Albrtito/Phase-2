from bst import BinarySearchTree
from bintree import BinaryNode
from bintree import BinaryTree
from dlist import DNode
from dlist import DList

"""Problem 2
Implement a function, create_tree, that receives as parameters two binary search trees, tree1 and tree2, 
of integers. It also receives a third parameter, opc, whose values can be 'merge', intersection', 
or 'difference':

• If opc is 'merge', it means that the function should create a new binary search tree containing the 
elements of both tree1 and tree2. Remember that in our implementation of the binary search tree we do 
not allow duplicate elements.
• If opc is 'intersection', it means that the function must create a new binary search tree containing 
only the elements that the trees, tree1 and tree2, have in common. If they have no elements in common, 
the function returns an empty tree (its root is None).
• If opc is 'difference', it means that the function must create a new binary search tree containing 
the elements of tree1 that are not in tree2. If all elements of tree1 are in tree2, the function returns
an empty tree (its root is None).
"""


class BST2(BinarySearchTree):
    def merge(self, tree1, tree2):
        """Merge: Return all elements"""

    def intersect(self, tree1, tree2):
        """Intersect: Return all elements in common"""

    def difference(self, tree1, tree2):
        """Difference: Return all elements of tree1 that are not on three2."""
