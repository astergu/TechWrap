"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

from __future__ import print_function


class Solution:
    def twoSum(self, nums, target):
        dct = dict()
        for i, item in enumerate(nums):
            x = target - item
            if x not in dct:
                dct[item] = i
            else:
                return [dct[x], i]
        return [None, None]


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))
