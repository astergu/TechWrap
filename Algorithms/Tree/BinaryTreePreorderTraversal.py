"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3

return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""

from TreeNode import TreeNode


class Solution(object):
    def preorderTraversal(self, root):
        """
        recursive implementation
        :param root:
        :return:
        """
        ans = []
        if root:
            ans.append(root.val)
            ans.extend(self.preorderTraversal(root.left))
            ans.extend(self.preorderTraversal(root.right))
        return ans

    def preorderTraversal_iter(self, root):
        """
        iterative implementation
        :param root:
        :return:
        """
        ans = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            ans.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    root.right = n1
    n1.left = n2

    s = Solution()
    print s.preorderTraversal_iter(root)