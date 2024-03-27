'''
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].
'''

from TreeNode import TreeNode, TreeNodeGenerator
from typing import Optional

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0

        def dfs(node, lo, hi):
            nonlocal range_sum
            if node is None:
                return 0
            if node.val >= lo and node.val <= hi:
                dfs(node.left, lo, hi)
                dfs(node.right, lo, hi)
                range_sum += node.val
            elif node.val < lo:
                dfs(node.right, lo, hi)
            elif node.val > hi:
                dfs(node.left, lo, hi)
        
        dfs(root, low, high)
        return range_sum


if __name__ == '__main__':
    sol = Solution()
    root = ["10","5","15","3","7","null","18"]
    low = 7
    high = 15
    tng = TreeNodeGenerator(root)
    print(sol.rangeSumBST(tng.get_root(), low, high))