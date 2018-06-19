#coding=utf8

"""
 Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

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
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= (ones & num)
            ones ^= num
            threes = ~(ones & twos)
            ones &= threes
            twos &= threes

        return ones


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()


if __name__ == '__main__':
    unittest.main()
