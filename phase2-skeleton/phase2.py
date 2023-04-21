"""
@author: EDA Team
"""

# Classes provided by EDA Team
from bintree import BinaryNode
from bst import BinarySearchTree


# Exercise #1
class BST2(BinarySearchTree):
    def find_dist_k(self, n: int, k: int) -> list:
        def find_dist_k(self, n: int, k: int) -> list:
            list = DList()

            def list_search(self, node: BinaryNode, elem: object, list: object) -> DList:
                """Recursive function"""
                if node == self.root:
                    list.head = DNode(node, None)
                    list.tail = DNode(node, None)
                list.tail.next = DNode(node, list.tail)
                list.tail = list.tail.next
                if node is None or node.elem == elem:
                    return list
                elif elem < node.elem:
                    return self.list_search(node.left, elem)
                elif elem > node.elem:
                    return self.list_search(node.right, elem)

            def search_down(self, node: BinaryNode, k: int, list: list, Dlist: object) -> list:
                if k == 0:
                    list += [node.elem]
                else:
                    if node.left is not None or node.right is not None:
                        loop = False
                    if node.left is not None:
                        Dlist.tail.next = DNode(node, Dlist.tail)
                        Dlist.tail = Dlist.tail.next
                        k -= 1
                        return search_down(node.left, k, list, Dlist)
                    if node.right is not None:
                        Dlist.tail.next = DNode(node, Dlist.tail)
                        Dlist.tail = Dlist.tail.next
                        k -= 1
                        return search_down(node.right, k, list, Dlist)
                    if (node.left is None and node.right is None) or loop:
                        k += 1
                        prev_node = Dlist.tail
                        if prev_node.right is not None and prev_node.right != node:
                            loop = False
                            return search_down(node.right, k, list, Dlist)
                        else:
                            loop = True
                            node = prev_node
                            Dlist.tail = Dlist.tail.prev
                            return search_down(node, k, list, Dlist)

            list = list_search(self.root, n, list)
            if list.size - 1 >= k:
                final_list = []
                if list.size - 1 == k:
                    final_list = [self.root.elem]
                k -= list.size
                if n > self.root.elem:
                    final_list += [search_down(list.tail.left, k, final_list, list)]
                    return final_list
                if n < self.root.elem:
                    final_list += [search_down(list.tail.right, k, final_list, list)]
                    return final_list
                if n == self.root.elem:
                    return search_down(list.tail.left, k, final_list, list) + search_down(list.tail.right, k,
                                                                                          final_list, list)
            elif list.size - 1 < k:
                return search_down(list.tail, k, final_list, list)


# Exercise #2
def create_tree(input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str) -> BinarySearchTree:
    # Here your code
    ...
    

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
    tree1.draw()

    # Build and draw second tree
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    tree2.draw()

    function_names = ["merge", "intersection", "difference"]

    for op_name in function_names:
        res = create_tree(tree1, tree2, op_name)
        print(f"-- Result for {op_name} method. #{res.size()} nodes")
        res.draw()
