"""
两个已排好序的数组，找出两者合并后的数组的中位数。

Example:
给出A=[1,2,3,4,5,6]和B=[2,3,4,5]，他们合并后给出的中位数是3.5 (3+4/2)

给出A=[1, 2, 3]和B=[4, 5], 合并以后的中位数为3.
"""


class Solution:
    def array_medium1(self, arr1, arr2):
        total = len(arr1) + len(arr2)
        medium = total // 2
        i, j, curr = 0, 0, 0
        medium_value = None
        while i < len(arr1) and j < len(arr2):
            if curr <= medium:
            if arr1[i] < arr2[j]:
                i += 1
                curr += 1
