# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def inorder_traversal(self, node):
        repr = ""
        if node:
            repr += self.inorder_traversal(node.left)
            repr += str(node.val) + " "
            repr += self.inorder_traversal(node.right)
        return repr.rstrip()

    def __eq__(self, other):
        return self.inorder_traversal(self) == self.inorder_traversal(other)