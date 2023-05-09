"""
@author: EDA Team
"""
from typing import Type

# Classes provided by EDA Team
from bintree import BinaryNode
from bst import BinarySearchTree
from dlist import DList
from dlist import DNode


# Exercise #1
class BST2(BinarySearchTree):
    ...

# Exercise #2
"""
Comments: 
+ Merge and difference functions use treeOut._root = tree1.root. This means that the changes made to treeOut will 
also be made to tree1. Both variables reference to the same memory slot. In order to create treeOut equal to tree1 but 
referenced to another memory slot a hard copy function could be created. This project does not create said function.
However it is interesting to point out this because of the usage of tree1 in the unittest to produce the expected 
value. In order to prevent errors. The expected value should be produced before assigning the create_tree output to 
treeOut. 
"""


def create_tree(input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str) -> Type[BinarySearchTree]:
    if opc == "Merge":
        return merge(input_tree1, input_tree2)  # Time complexity: O( n * log2 n)
    elif opc == "Intersect":
        return intersect(input_tree1, input_tree2)  # Time complexity: O( n * log2 n)
    elif opc == "Difference":
        return difference(input_tree1, input_tree2)  # Time complexity: O( n * log2 n)


def merge(tree1: BinarySearchTree, tree2: BinarySearchTree):
    """Merge: Return all elements without repetition"""
    treeOut = BinarySearchTree()
    # treeOut and tree1 reference to the same memory position.
    treeOut._root = tree1._root
    list2 = tree2.inorder_list()  # O(n);  n -> Number of nodes of tree2
    for i in range(len(list2)):  # O(n)
        treeOut.insert(list2.getAt(i))  # O(n * log2 m);  m -> Number of nodes of treeOut
    return treeOut


# The intersect and difference functions without the AVL can easily create list like trees
def intersect(tree1: BST2, tree2: BST2):
    """Intersect: Return all elements repeated in both trees"""
    treeOut = BinarySearchTree()
    list2 = tree2.inorder_list()  # O(n);  n -> Number of nodes of tree2
    for i in range(len(list2)):  # O(n)
        if tree1.search(list2.getAt(i)):  # O(n * log2 s); s -> Number of nodes of tree1
            treeOut.insert(list2.getAt(i))  # O(n * log2 m);  m -> Number of nodes of treeOut
    return treeOut


def difference(tree1: BST2, tree2: BST2):
    """Merge: Return all elements without repetition"""
    treeOut = BinarySearchTree()
    # treeOut and tree1 reference to the same memory position.
    treeOut._root = tree1._root
    list2 = tree2.inorder_list()  # O(n);  n -> Number of nodes of tree2
    for i in range(len(list2)):  # O(n)
        if tree1.search(list2.getAt(i)):  # O(n * log2 s); s -> Number of nodes of tree1
            treeOut.remove(list2.getAt(i))  # O(n * log2 s);
    return treeOut


"""
# Some usage examples
if __name__ == '__main__':
    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11]
    input_list_01 = [5, 12, 2, 1, 3, 9]
    input_list_02 = [9, 3, 21]

    # Build and draw first tree
    tree1 = BinarySearchTree()
    for x in input_list_01:
        tree1.insert(x)
    tree1.display()
    print("----------------------")
    # Build and draw second tree
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    tree2.display()

    function_names = ["merge", "intersection", "difference"]

    for op_name in function_names:
        res = create_tree(tree1, tree2, op_name)
        print(f"-- Result for {op_name} method. #{res.size()} nodes")
        res.draw()
"""