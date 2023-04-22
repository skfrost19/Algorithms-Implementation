import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
class BinarySearchTree:
    def __init__(self) -> None:
        self.head = None

    def create_node(self, val):
        return Node(val)
    
    def add(self, val):
        self.head = self.__add_helper(self.head, Node(val))
    
    def __add_helper(self, root, node):
        if root == None:
            return node
        if root.val > node.val:
            root.left = self.__add_helper(root.left, node)
        else:
            root.right = self.__add_helper(root.right, node)
        return root
    
    def print_tree(self):
        # inorder
        self.__print_tree_helper(self.head)

    def __print_tree_helper(self, head):
        if head == None:
            return
        self.__print_tree_helper(head.left)
        print(head.val , " ")
        self.__print_tree_helper(head.right)

class Test(unittest.TestCase):
    def test_add(self):
        bst = BinarySearchTree()
        bst.add(5)
        bst.add(2)
        bst.add(7)
        bst.add(1)
        bst.add(3)
        bst.add(6)
        bst.add(8)
        bst.print_tree()

if __name__ == "__main__":
    unittest.main()