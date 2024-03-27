'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

'''

from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.size = 1

class UnionFind(object):
    def find(self, node):
        if node.parent != node:
            node.parent = self.find(node.parent)
        return node.parent
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 != p2:
            p2.parent = p1
            p1.size += p2.size
        return p1.size

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind()
        nodes = {}
        max_size = 0
        for num in nums:
            if num not in nodes:
                node = Node(num)
                nodes[num] = node
                size = 1
                if num + 1 in nodes:
                    size = uf.union(node, nodes[num + 1])
                if num - 1 in nodes:
                    size = uf.union(node, nodes[num - 1])
                max_size = max(max_size, size)
        
        return max_size
    
    def longestConsecutive2(self, nums):
        nums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in nums:
                nextNum = num + 1
                while nextNum in nums:
                    nextNum += 1
                res = max(res, nextNum - num)
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [100,4,200,1,3,2]
    print(sol.longestConsecutive(nums))