"""
Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i. 
Return -1 if no such i exists.
"""


class Solution(object):
    def fixedPoint(self, A):
        for i, item in enumerate(A):
            if i == item:
            return i
        return -1
