#coding=utf8

"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

import unittest


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans = ans ^ num
        return ans


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        nums = [2, 3, 3, 1, 2, 4, 4]
        ret = self.s.singleNumber(nums)
        self.assertEqual(ret, 1)


if __name__ == '__main__':
    unittest.main()
