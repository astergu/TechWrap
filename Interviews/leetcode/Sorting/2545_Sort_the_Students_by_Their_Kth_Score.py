'''
There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score, where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam. The matrix score contains distinct integers only.

You are also given an integer k. Sort the students (i.e., the rows of the matrix) by their scores in the kth (0-indexed) exam from the highest to the lowest.

Return the matrix after sorting it.
'''

from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        kth = [(i, score[i][k]) for i in range(len(score))]
        kth.sort(key=lambda x: x[1], reverse=True)
        ans = []
        for i in kth:
            ans.append(score[i[0]])
        return ans

if __name__ == '__main__':
    sol = Solution()
    score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
    k = 2
    print(sol.sortTheStudents(score, k))