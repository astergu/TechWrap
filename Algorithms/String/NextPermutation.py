#!/usr/bin/env python

class Solution(object):
    def nextPermutation(self, nums):
	size = len(nums)
	for i in xrange(size - 1, -1, -1):
	    if nums[i - 1] < nums[i]:
		break

	if i > 0:  # has answer
	    for j in xrange(size - 1, -1, -1):
		if nums[j] > nums[i - 1]:
		    nums[i - 1], nums[j] = nums[j], nums[i - 1]
		    break

	for x in xrange((size - i) / 2):
	    nums[i + x], nums[size - x - 1] = nums[size - x - 1], nums[i + x]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1]
    s.nextPermutation(nums)
    print nums
