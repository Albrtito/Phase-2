"""
@author: EDA Team
"""

# Classes provided by EDA Team
from bintree import BinaryNode
from bst import BinarySearchTree


# Exercise #1
class BST2(BinarySearchTree):
    def find_dist_k(self, n: int, k: int) -> list:
        # Here your code
        ...


# Exercise #2
def create_tree(input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str) -> BinarySearchTree:
    if opc == "Merge":
        return merge(input_tree1,input_tree2)
    elif opc == "Intersect":
        return intersect(input_tree1,input_tree2)
    elif opc == "Difference":
        return difference(input_tree1,input_tree2)


def merge(self, tree1: BST2, tree2: BST2):
    """Merge: Return all elements without repetition"""
    treeOut = BST2
    treeOut._root = tree1._root
    for elem in tree2.inorder_list():
        treeOut.insert(elem)
    return treeOut

def intersect(self, tree1: BST2, tree2: BST2):
    """Merge: Return all elements without repetition"""
    treeOut = BST2
    treeOut._root = tree1._root
    for elem in tree2.inorder_list():
        treeOut.insert(elem)
    return treeOut

def difference(self, tree1: BST2, tree2: BST2):
    """Merge: Return all elements without repetition"""
    treeOut = BST2
    treeOut._root = tree1._root
    for elem in tree2.inorder_list():
        treeOut.insert(elem)
    return treeOut

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
