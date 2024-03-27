'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
'''

from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)): # row
            for j in range(len(grid[0])): # column
                pass


if __name__ == '__main__':
    sol = Solution()
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    print(sol.equalPairs(grid))