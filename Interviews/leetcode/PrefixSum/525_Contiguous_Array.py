'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

'''

from typing import List
from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}
        sum_val = 0
        max_len = 0
        for i, n in enumerate(nums):
            sum_val += 1 if n == 1 else -1
            if sum_val == 0:
                max_len = i + 1
            elif sum_val in mp:
                max_len = max(max_len, i - mp[sum_val])
            else:
                mp[sum_val] = i
            print(i, n, sum_val, max_len, mp)
        return max_len


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 1, 0, 1]
    print(sol.findMaxLength(nums))
