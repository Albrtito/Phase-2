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
    def find_dist_k(self, n: int, k: int) -> list:
        if k == 0:
            return []
        Dlist = DList()

        def list_search(node: BinaryNode, elem: object, list: object) -> DList:
            if node == self.root:
                list._head = DNode(node)
                list._size = 1
                list._tail = list._head
            else:
                list._tail = DNode(node, list._tail)
                list._size += 1
            if node is None or node.elem == elem:
                return list
            elif elem < node.elem:
                return list_search(node.left, elem, list)
            elif elem > node.elem:
                return list_search(node.right, elem, list)

        # Works
        def search_down(node: BinaryNode, k: int, list, first_node: int):

            if k == 0:
                return node.elem
            else:
                if node.left is not None:
                    k -= 1
                    list += [search_down(node.left, k, list, first_node)]
                    k += 1
                if node.right is not None:
                    k -= 1
                    list += [search_down(node.right, k, list, first_node)]
                    k += 1
                if node.elem == first_node:
                    return list

        list = list_search(self.root, n, Dlist)
        end_list = []
        if list._tail.elem is None:
            return []
        else:
            end_list = search_down(list._tail.elem, k, end_list, list._tail.elem.elem)
            while list._size != 1 and k > 0:
                if list._tail.elem.elem < list._tail.prev.elem.elem:
                    list._tail = list._tail.prev
                    list._size -= 1
                    k -= 1
                    if k == 0:
                        end_list += [list._tail.elem.elem]
                    k -= 1
                    end_list += [search_down(list._tail.elem.right, k, end_list, list._tail.elem.elem)]
                elif list._tail.elem.elem > list._tail.prev.elem.elem:
                    list._tail = list._tail.prev
                    list._size -= 1
                    k -= 1
                    if k == 0:
                        end_list += [list._tail.elem.elem]
                    k -= 1
                    end_list += [search_down(list._tail.elem.left, k, end_list, list._tail.elem.elem)]
            final_list = []
            for e in end_list:
                if e != None:
                    final_list += [e]

            return final_list


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
    if opc.lower() == "merge":

        return merge(input_tree1, input_tree2) # Time complexity: O( n * log2 n)
    elif opc.lower() == "intersection":
        return intersect(input_tree1, input_tree2)  # Time complexity: O( n * log2 n)
    elif opc.lower() == "difference":
        return difference(input_tree1, input_tree2)  # Time complexity: O( n * log2 n)


def merge(tree1: BinarySearchTree, tree2: BinarySearchTree):
    """Merge: Return all elements without repetition"""
    treeOut = BinarySearchTree()
    # treeOut and tree1 reference to the same memory position.
    treeOut._root = tree1._root
    list2 = tree2.inorder_list()  # O(n);  n -> Number of nodes of tree2
    for i in range(len(list2)):  # O(n)
        treeOut.insert(list2.getAt(i)) # O(n * log2 m);  m -> Number of nodes of treeOut
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
