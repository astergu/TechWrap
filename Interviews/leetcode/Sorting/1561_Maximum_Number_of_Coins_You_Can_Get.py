'''
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

    In each step, you will choose any 3 piles of coins (not necessarily consecutive).
    Of your choice, Alice will pick the pile with the maximum number of coins.
    You will pick the next pile with the maximum number of coins.
    Your friend Bob will pick the last pile.
    Repeat until there are no more piles of coins.

Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.
'''

from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        print(piles)
        ret = [piles[i+1] for i in range(0, n-1, 2)]
        return sum(ret[:n//3])

if __name__ == '__main__':
    sol = Solution()
    piles = [9,8,7,6,5,1,2,3,4]
    print(sol.maxCoins(piles))