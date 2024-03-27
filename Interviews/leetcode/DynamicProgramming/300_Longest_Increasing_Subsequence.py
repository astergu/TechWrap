'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''

from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Time complexity: O(N^2)
        """
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    def lengthOfLISLogNComplexity(self, nums: List[int]) -> int:
        """
        Time complexity: O(NlogN)
        """
        dp = []

        for n in nums:
            insert_idx = bisect.bisect_left(dp, n)
            if insert_idx == len(dp):
                dp.append(n)
            else:
                dp[insert_idx] = n

        return len(dp)


if __name__ == '__main__':
    sol = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(sol.lengthOfLIS(nums))