#coding=utf8

"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""

import unittest


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
            Can we do it on O(N) time?
        """
        prefixsum, ret = 0, 0
        cache = dict()
        cache[0] = 1
        for i in xrange(len(nums)):
            prefixsum += nums[i]
            ret += cache.get(prefixsum - k, 0)
            cache[prefixsum] = cache.get(prefixsum, 0) + 1
        return ret

    def naive_subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Time complexity: O(N^2)
        Space complexity: O(N^2)
        """
        arraysum = [[0] * len(nums) for i in range(len(nums))]
        for i in xrange(len(nums)):
            arraysum[i][i] = nums[i]

        ret = 0
        for i in xrange(len(nums)):
            for j in xrange(i, len(nums)):
                arraysum[i][i] = nums[i]
                if j != i:
                    arraysum[i][j] = arraysum[i][j - 1] + nums[j]
                print "array[%d][%d]: %d" % (i, j, arraysum[i][j])
                if arraysum[i][j] == k:
                    ret += 1
        return ret


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        nums = [1, 1, 1]
        k = 2
        self.assertEqual(self.s.subarraySum(nums, k), 2)


if __name__ == '__main__':
    #s = Solution()
    #print s.subarraySum([1, 2, 3], 3)
    unittest.main()