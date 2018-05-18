#coding=utf8

"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: [2,3,1,2,4,3], s = 7
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

"""

import unittest


class Solution(object):
    def minSubarrayLen(self, s, nums):
        """
           :type s: int
           :type nums: List[int]
           :rtype: int
        """
        start, end = 0, 0
        curr_sum = 0
        ret = None
        while end < len(nums):
            curr_sum += nums[end]
            end += 1
            while curr_sum >= s:
                ret = min(end - start, ret) if ret else end - start
                curr_sum -= nums[start]
                start += 1
        return ret if ret else 0


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        input = [2, 3, 1, 2, 4, 3]
        s = 7
        output = 2
        self.assertEqual(self.s.minSubarrayLen(s, input), output)

    def test2(self):
        input = []
        s = 2
        output = 0
        self.assertEqual(self.s.minSubarrayLen(s, input), output)

    def test3(self):
        input = [1, 1, 2, 3]
        s = 2
        output = 1
        self.assertEqual(self.s.minSubarrayLen(s, input), output)


if __name__ == '__main__':
    unittest.main()
