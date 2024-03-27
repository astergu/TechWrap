'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
'''
from typing import Optional
from TreeNode import TreeNode, TreeNodeGenerator

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key == root.val: # found
            if not root.left and not root.right:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            else: # 找左子树的最大或者右子树的最小来作为根节点
                min_node = self.get_min(root.right)
                root.right = self.deleteNode(root.right, min_node.val)
                min_node.left = root.left
                min_node.right = root.right
                root = min_node
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        return root

    def get_min(self, root):
        while root.left:
            root = root.left
        return root


if __name__ == '__main__':
    sol = Solution()
    lst = ["50", "30", "70", "null", "40", "60", "80"]
    key = 50
    tng = TreeNodeGenerator(lst)
    #tng.get_root().level_order_traversal()
    ret = sol.deleteNode(tng.get_root(), key)
    ret.level_order_traversal()