#coding=utf8

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            nres = []
            for perm in res:
                n = len(perm)
                for i in xrange(n + 1):
                    nres.append(perm[:i] + [num] + perm[i:])
                    if i < n and num == perm[i]:
                        break
            res = nres
        return res


if __name__ == '__main__':
    lst = [1, 1, 2]
    s = Solution()
    print s.permuteUnique(lst)
