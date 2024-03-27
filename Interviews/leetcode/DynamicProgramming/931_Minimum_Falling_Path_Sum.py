'''
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

'''

from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        MAX = 10000
        row_num, col_num = len(matrix), len(matrix[0])
        memo = [[MAX] * col_num for i in range(row_num)]
        
        def dp(i, j):
            #print("dp [{}][{}]".format(i, j))
            if i < 0 or j < 0 or i >= row_num or j >= col_num:
                return MAX
            if i == 0:
                memo[i][j] = matrix[i][j]
        
            if (memo[i][j] != MAX):
                return memo[i][j]
            memo[i][j] = min(memo[i][j], 
                             min(dp(i-1, j), 
                                 dp(i-1, j-1), 
                                 dp(i-1, j+1)) + matrix[i][j]) 

            return memo[i][j] 


        for j in range(col_num):
            dp(row_num - 1, j)

        return min(memo[row_num-1])


if __name__ == '__main__':
    sol = Solution()
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    print(sol.minFallingPathSum(matrix))