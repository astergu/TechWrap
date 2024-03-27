'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
'''

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        triplet = []
        for i in range(len(nums)):
            print("[num] {}, [triplet] {}".format(nums[i], triplet))
            if len(triplet) == 0:
                triplet.append(nums[i])
            while len(triplet) > 0 and nums[i] < triplet[-1]:
                triplet.pop()
            triplet.append(nums[i])

        print(triplet) 
        return len(triplet) >= 3


if __name__ == '__main__':
    sol = Solution()
    nums = [20, 100, 10, 12, 5, 13]
    print(sol.increasingTriplet(nums))