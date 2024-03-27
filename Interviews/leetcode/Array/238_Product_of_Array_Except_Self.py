'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = 1
        postfix_product = 1
        res = [0] * n
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]
        print(res) 
        for i in range(n - 1, -1, -1):
            res[i] *= postfix_product
            postfix_product *= nums[i]
        
        return res

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4]
    print(sol.productExceptSelf(nums))