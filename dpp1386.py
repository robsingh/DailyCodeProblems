"""
Asked by DropBox.

Given the root is a binary search tree, find the second largest node in the tree.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_second_largest(root):
    if root is None or (root.left is None and root.right is None):
        return None
    
    def find_largest(node):
        while node.right is not None:
            node = node.right
        return node
    
    # case 1: largest node has a left subtree.
    if root.left is not None and root.right is None:
        return find_largest(root.left)
    
    # case 2: largest node doesn't have a left subtree
    if root.right is not None and root.right.left is None and root.right.right is None:
        return root
    
    # case 3: recrusively search for second largest node
    return find_second_largest(root.right)

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

second_largest = find_second_largest(root)

if second_largest is not None:
    print("Second largest node value is: ", second_largest.value)
else:
    print("No second largest node!!!")
