"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        zeros = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            ans = max(ans, r - l + 1 - zeros)
        
        return ans - 1 if ans == len(nums) else ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 0, 1]
    print(sol.longestSubarray(nums))