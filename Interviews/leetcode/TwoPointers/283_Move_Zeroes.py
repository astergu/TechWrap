'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast, slow = 0, 0
        while fast != len(nums):
            if nums[fast] != 0:
                if fast != slow:
                    nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1
            fast += 1
        
        print(nums)
        

if __name__ == '__main__':
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)