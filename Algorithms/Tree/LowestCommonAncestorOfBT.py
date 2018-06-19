class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path_to_p = self.path_to(root, p)
        path_to_q = self.path_to(root, q)
        ret = None
        while path_to_p and path_to_q:
            pop_p = path_to_p.pop()
            pop_q = path_to_q.pop()
            if pop_p.val == pop_q.val:
                ret = pop_p
            else:
                break
        return ret


    def path_to(self, root, x):
        if not root:
            return None
        if root.val == x.val:
            return [x]
        left = self.path_to(root.left, x)
        if left:
            left.append(root)
            return left
        right = self.path_to(root.right, x)
        if right:
            right.append(root)
            return right
        return None
