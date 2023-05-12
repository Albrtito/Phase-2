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
    if opc == "Merge":

        return merge(input_tree1, input_tree2) # Time complexity: O( n * log2 n)
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
        treeOut.insert(list2.getAt(i)) # O(n * log2 m);  m -> Number of nodes of treeOut
        rebalanced(treeOut.search(list2.getAt(i)))
    return treeOut


# The intersect and difference functions without the AVL can easily create list like trees
def intersect(tree1: BST2, tree2: BST2):
    """Intersect: Return all elements repeated in both trees"""
    treeOut = BinarySearchTree()
    list2 = tree2.inorder_list()  # O(n);  n -> Number of nodes of tree2
    for i in range(len(list2)):  # O(n)
        if tree1.search(list2.getAt(i)):  # O(n * log2 s); s -> Number of nodes of tree1
            treeOut.insert(list2.getAt(i))  # O(n * log2 m);  m -> Number of nodes of treeOut
            rebalanced(treeOut.search(list2.getAt(i)))
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
            rebalanced(treeOut.search(list2.getAt(i)))
    return treeOut


def rebalanced(node: BinaryNode) -> BinaryNode:
    # O(n)
    if abs(balance_factor(node)) <= 1:
        return node  # the node is already balanced, we do nothing

    # print('balancing ', node.elem)

    height_left = _height(node.left)
    height_right = _height(node.right)

    # the left branch is larger than the right branch, so
    # we have to do a right rotation
    if height_left > height_right:  # right rotate
        # as it is greater, node.left cannot be None,
        height_left_left = _height(node.left.left)
        height_left_right = _height(node.left.right)
        if height_left_left < height_left_right:
            # print(' double first left rotation on: ', node.elem)
            node.left = left_rotate(node.left)
        # print('right rotation on ', node.elem)
        node = right_rotate(node)
    else:
        # left rotate
        height_right_left = _height(node.right.left)
        height_right_right = _height(node.right.right)
        if height_right_right < height_right_left:  # double rotation (right - left)
            # print(' double first right rotation on: ', node.elem)
            node.right = right_rotate(node.right)
        # print('left rotation on ', node.elem)
        node = left_rotate(node)
    return node


def right_rotate(node: BinaryNode) -> BinaryNode:
    """balance node by right rotation """
    # its child left becomes the new root (and we will return it)
    new_root = node.left  # it will be the new root
    # we save the right child of new_root (because it will become the left child of node)
    subtree = new_root.right
    # node becomes the right child of new_root
    new_root.right = node
    # the (old) right child of new_root has to be the left child of node
    node.left = subtree
    # print(new_root.left.elem,new_root.elem,new_root.right.elem)
    return new_root


def left_rotate(node: BinaryNode) -> BinaryNode:
    """balance node applying left rotation"""
    # print("left rotation on ", node.key)
    # its right child becomes the new root of the subtree
    # Also, the function will return new_root
    new_root = node.right
    # we save the left child of new_root, because
    # it becomes the right child of node
    subtree = new_root.left

    # we have to update the parent for newRoot
    new_root.left = node
    # now, the old left child of new_root has to be
    # the right child of node
    node.right = subtree

    return new_root


def balance_factor(node: BinaryNode) -> int:
    """returns the balance factor of node.
     It is the height of its right subtree minus
     the height of its left subtree"""
    if node is None:
        return 0
    else:
        return _height(node.right) - _height(node.left)


def _height(node: BinaryNode) -> int:
    """return the height of node"""
    if node is None:
        return -1
    else:
        return 1 + max(_height(node.left), _height(node.right))


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
