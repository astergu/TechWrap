'''
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

Example 2:

Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].

'''
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = 0, 0
        arr = []
        i = 0
        while i < len(nums):
            if i % 2 == 0: # expects positive number
                while pos < len(nums) - 1 and nums[pos] < 0:
                    pos += 1
                arr.append(nums[pos])
                pos += 1
            else:
                while neg < len(nums) and nums[neg] > 0:
                    neg += 1
                arr.append(nums[neg])
                neg += 1
            i += 1
        
        return arr

    def rearrangeArray2(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for num in nums:
            if num >= 0:
                pos.append(pos)
            else:
                neg.append(num)
        
        nums[0:len(pos) * 2: 2] = pos
        nums[1:len(neg) * 2: 2] = neg

        return nums

if __name__ == '__main__':
    sol = Solution()
    nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
    print(sol.rearrangeArray(nums))