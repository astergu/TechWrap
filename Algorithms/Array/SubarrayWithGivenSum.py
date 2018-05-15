#coding=utf8

"""
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number.
"""

import unittest


class Solution(object):
    def subarray_with_given_sum(self, nums, k):
        start, end = 0, 0
        while end < len(nums) + 1:
            range_sum = sum(nums[start:end])
            if range_sum == k:
                return [start + 1, end]
            elif range_sum > k:
                start += 1
                continue
            end += 1
        return []


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        nums = [1, 2, 3, 4]
        k = 5
        ret = [2, 3]
        self.assertListEqual(self.s.subarray_with_given_sum(nums, k), ret)

    def test2(self):
        nums = [1, 2, 3, 7, 5]
        k = 12
        ret = [2, 4]
        self.assertListEqual(self.s.subarray_with_given_sum(nums, k), ret)

    def test3(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        k = 15
        ret = [1, 5]
        self.assertListEqual(self.s.subarray_with_given_sum(nums, k), ret)

    def test4(self):
        nums = [135, 101, 170, 125, 79, 159, 163, 65, 106, 146,\
                82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, \
                154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139,\
                70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
        k = 468
        ret = [38, 42]
        self.assertListEqual(self.s.subarray_with_given_sum(nums, k), ret)


if __name__ == '__main__':
    unittest.main()