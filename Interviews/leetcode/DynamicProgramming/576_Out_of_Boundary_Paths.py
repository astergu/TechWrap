"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 10^9 + 7.
"""

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        Time complexity: O(Nmn)
        Space complexity: O(mn)
        """
        M = pow(10, 9) + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        count = 0

        for moves in range(1, maxMove + 1):
            temp = [[0] * n for _ in range(m)]

            for i in range(m):  # row
                for j in range(n):  # column
                    if i == m - 1 or j == n - 1 or i == 0 or j == 0:
                        count = (count + dp[i][j]) % M
                    temp[i][j] = (
                        ((dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < m - 1 else 0)) % M +
                        ((dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < n - 1 else 0)) % M
                    ) % M                   
            
            dp = temp
        
        return count


if __name__ == '__main__':
    sol = Solution()
    m = 2
    n = 2
    maxMove = 2
    startRow = 0
    startColumn = 0
    print(sol.findPaths(m, n, maxMove, startRow, startColumn))