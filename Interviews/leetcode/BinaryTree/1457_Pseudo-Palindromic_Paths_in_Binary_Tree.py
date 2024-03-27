'''
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
'''

from TreeNode import TreeNode, TreeNodeGenerator
from typing import Optional

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, p):
            nonlocal ans
            if not node:
                return
            x = node.val
            p ^= (1 << x)
            print("[x] {} {}, [p] {} {}".format(x, bin(x), p, bin(p)))
            if not node.left and not node.right: # leaf node
                if p.bit_count() <= 1:
                    ans += 1
                return
            dfs(node.left, p)
            dfs(node.right, p)
        
        p = 0
        dfs(root, p)
        return ans


if __name__ == '__main__':
    sol = Solution()
    lst = ["2","3","1","3","1","null","1"]
    tng = TreeNodeGenerator(lst)
    root = tng.get_root()
    print(sol.pseudoPalindromicPaths(root))