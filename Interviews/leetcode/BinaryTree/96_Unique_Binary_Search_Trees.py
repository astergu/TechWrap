'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
'''

class Solution:
    def numTrees(self, n: int) -> int:
        return self.count_trees(1, n)

    def count_trees(self, low, high):
        if low > high:
            return 1
        

if __name__ == '__main__':
    sol = Solution()
    n = 3
    print(sol.numTrees(n))