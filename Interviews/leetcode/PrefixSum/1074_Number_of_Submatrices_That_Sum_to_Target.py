'''
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:

Input: matrix = [[904]], target = 0
Output: 0

'''

from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Time complexity: O(mmn)
        Space complexity: O(mn)
        """
        m, n = len(matrix), len(matrix[0])
        sum_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        count = 0

        for i in range(m):
            for j in range(n):
                sum_matrix[i + 1][j + 1] += matrix[i][j] + sum_matrix[i][j + 1] + sum_matrix[i + 1][j] - sum_matrix[i][j]
        
        for r1 in range(1, m + 1):
            for r2 in range(r1, m + 1):
                sum_count = {0: 1}
                cur_sum = 0
                for c in range(1, n + 1):
                    cur_sum = sum_matrix[r2][c] - sum_matrix[r1-1][c]
                    count += sum_count.get(cur_sum - target, 0)
                    sum_count[cur_sum] = sum_count.get(cur_sum, 0) + 1

        return count


if __name__ == '__main__':
    sol = Solution()
    matrix = [[0,1,0],[1,1,1],[0,1,0]]
    target = 0
    print(sol.numSubmatrixSumTarget(matrix, target))