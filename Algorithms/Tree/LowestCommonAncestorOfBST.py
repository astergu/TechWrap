from TreeNode import TreeNode


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(6)
    n1 = TreeNode(2)
    n2 = TreeNode(0)
    n3 = TreeNode(4)
    n4 = TreeNode(3)
    n5 = TreeNode(5)
    n6 = TreeNode(8)
    n7 = TreeNode(7)
    n8 = TreeNode(9)
    root.left, root.right = n1, n6
    n1.left, n1.right = n2, n3
    n3.left, n3.right = n4, n5
    n6.left, n6.right = n7, n8
    ret = s.lowestCommonAncestor(root, n1, n6)
    print ret.val
