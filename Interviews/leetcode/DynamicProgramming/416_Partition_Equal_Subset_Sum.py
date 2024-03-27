'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False

        dp = [True] + [False] * s
        for i in nums:
            for j in range(s, -1, -1):
                if j - i >= 0:
                    dp[j] = (dp[j] or dp[j - i]) 
                    print("[i] {}, [j] {}, [dp_j] {}, [dp_j-i] {}".format(i, j, dp[j], dp[j-i]))

        return dp[s]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 5]
    print(sol.canPartition(nums))