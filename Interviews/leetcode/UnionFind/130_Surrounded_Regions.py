'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

'''

from typing import List

class UnionFind(object):
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.size = [1] * n

    def union(self, i, j):
        i, j = self.find(i), self.find(j)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]

    def find(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, i, j):
        return self.find(i) == self.find(j)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        
        m, n = len(board), len(board[0])
        uf = UnionFind(m * n + 1)
        dummy = m * n
        # handle border 'O's
        for i in range(m):
            if board[i][0] == 'O':
                uf.union(i * n, dummy)
            if board[i][n-1] == 'O':
                uf.union(i * n + n - 1, dummy)
        
        for j in range(n):
            if board[0][j] == 'O':
                uf.union(j, dummy)
            if board[m-1][j] == 'O':
                uf.union(n * (m-1) + j, dummy)
        
        d = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == 'O':
                    for k in range(4):
                        x = i + d[k][0]
                        y = j + d[k][1]
                        if board[x][y] == 'O':
                            uf.union(x * n + y, i * n + j)
        
        for i in range(m - 1):
            for j in range(n - 1):
                if not uf.connected(dummy, i * n + j):
                    board[i][j] = 'X'
            


if __name__ == '__main__':
    sol = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol.solve(board)
    print(board)