#coding=utf8


"""
DescriptionHintsSubmissionsDiscussSolution

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

分析：
1. distinct，不需要考虑重复
2. return all possible permutations. 不需要考虑返回元素的顺序。

Possible Followup:
1. not distinct
2. return ascending order of permutations
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        recursive solution:
        Time complexity: O(n * n!)
        Space complexity: O(n!)

        Not efficient enough!
        """
        if not nums:
            return []
        elif len(nums) == 1:
            return [nums]
        return [[num] + p for i, num in enumerate(nums) for p in self.permute(nums[:i] + nums[i+1:])]

    def permute_advance(self, nums):
        """
        Time complexity: O(n * n!)
        Space complexity: O(n)
        """
        res = [[]]
        for num in nums:
            nres = []
            for perm in res:
                n = len(perm)
                for i in xrange(n + 1):
                    nres.append(perm[:i] + [num] + perm[i:])
            res = nres
        return res


"""
Brainstorm test
____________________________________

nums = [1, 2, 3]
- num = 1,  res = [[]]
    - res = [[1]]
- num = 2, res = [[1]]
    - res = [[[1, 2], [2, 1]]
- nums = 3, res = [[[1, 2], [2, 1]]
"""

if __name__ == '__main__':
    lst = [1, 2, 3]
    s = Solution()
    print s.permute_advance(lst)

