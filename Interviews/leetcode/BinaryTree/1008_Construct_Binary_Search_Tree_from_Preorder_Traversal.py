'''
Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.
'''

from TreeNode import TreeNode
from typing import List, Optional

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for i in preorder[1:]:
            if i < stack[-1].val:
                left = TreeNode(i)
                stack[-1].left = left
                stack.append(left)
            else:
                while stack and stack[-1].val < i:
                    tmp = stack.pop()
                right = TreeNode(i)
                tmp.right = right
                stack.append(right)
        
        return root
            

        

if __name__ == '__main__':
    sol = Solution()
    preorder = [8,5,1,7,10,12]
    node = sol.bstFromPreorder(preorder)