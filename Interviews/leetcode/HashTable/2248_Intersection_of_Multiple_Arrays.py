'''
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.
 

Example 1:

Input: nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
Output: [3,4]
Explanation: 
The only integers present in each of nums[0] = [3,1,2,4,5], nums[1] = [1,2,3,4], and nums[2] = [3,4,5,6] are 3 and 4, so we return [3,4].
Example 2:

Input: nums = [[1,2,3],[4,5,6]]
Output: []
Explanation: 
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
'''
from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        from collections import defaultdict
        s = defaultdict(int)
        for n in nums:
            for i in n:
                s[i] += 1
        
        res = []
        for k, v in s.items():
            if v >= len(nums):
                res.append(k)
        return sorted(res)

    """
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        ll = []
        for x in nums:
            ll.extend(x)
        
        from collections import Counter
        res = [k for k, v in Counter(ll).items() if v >= n]
        return sorted(res)
    """

if __name__ == '__main__':
    sol = Solution()
    nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
    print(sol.intersection(nums))