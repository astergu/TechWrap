#coding=utf8

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

import unittest


class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()
        print nums
        max_len, length = 1, 1
        for i in xrange(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                length += 1
            else:
                length = 1
            if length > max_len:
                max_len = length
        return max_len

    def longestConsecutiveFast(self, nums):
        used = {}
        for num in nums:
            used[num] = False

        longest = 0
        for num in nums:
            if used[num]:
                continue

            length = 1
            used[num] = True
            i = num + 1
            while i in used:
                used[i] = True
                i += 1
                length += 1

            i = num - 1
            while i in used:
                used[i] = True
                i -= 1
                length += 1

            longest = max(length, longest)

        return longest


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        nums = [100, 4, 200, 1, 3, 2]
        ret = self.s.longestConsecutive(nums)
        self.assertEqual(ret, 4)

    def test2(self):
        nums = [5, 1, 2, 3, 4]
        ret = self.s.longestConsecutive(nums)
        self.assertEqual(ret, 5)

    def test3(self):
        nums = [1, 2, 0, 1]
        ret = self.s.longestConsecutive(nums)
        self.assertEqual(ret, 3)

    def test4(self):
        nums = [9,1,4,7,3,-1,0,5,8,-1,6]
        ret = self.s.longestConsecutive(nums)
        self.assertEqual(ret, 7)


if __name__ == '__main__':
    unittest.main()
