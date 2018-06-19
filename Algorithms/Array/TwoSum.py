#coding=utf8

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dct:
                return [i, dct[diff]]
            dct[num] = i
        return []


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        nums = [2, 7, 11, 15]
        target = 9
        ret = self.s.twoSum(nums, target)
        self.assertListEqual(ret, [1, 0])

    def test2(self):
        nums = [3, 6, 3]
        target = 6
        ret = self.s.twoSum(nums, target)
        self.assertListEqual(ret, [2, 0])


if __name__ == '__main__':
   unittest.main()