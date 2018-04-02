"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3

return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
"""

from TreeNode import TreeNode


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root:
            ans.extend(self.inorderTraversal(root.left))
            ans.append(root.val)
            ans.extend(self.inorderTraversal(root.right))
        return ans

    def inorderTraversal_iter(self, root):
        stack = []
        ans = []
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                ans.append(p.val)
                p = p.right
        return ans

if __name__ == '__main__':
    root = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    root.right = n1
    n1.left = n2

    s = Solution()
    print s.inorderTraversal(root)