"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3



return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

"""

from TreeNode import TreeNode


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root:
            ans.extend(self.postorderTraversal(root.left))
            ans.extend(self.postorderTraversal(root.right))
            ans.append(root.val)
        return ans

    def postorderTraversal_iter(self, root):
        ans, stack = [], []
        p, q = root, None
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                if not node.right or node.right == q:
                    ans.append(node.val)
                    q = node
                else:
                    stack.append(node)
                    p = node.right
        return ans

    def postorderTraversal_iter2(self, root):
        ans, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    ans.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return ans

if __name__ == '__main__':
    root = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(4)
    root.right = n1
    n1.left, n1.right = n2, n3

    s = Solution()
    print s.postorderTraversal_iter(root)