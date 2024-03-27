'''
You are given a 0-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

 

Example 1:

Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]
Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.

Example 2:

Input: nums = [1,7,6,18,2,1], limit = 3
Output: [1,6,7,18,1,2]
Explanation: Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.

Example 3:

Input: nums = [1,7,28,19,10], limit = 3
Output: [1,7,28,19,10]
Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.

'''

from typing import List
from collections import defaultdict
import heapq
from collections import deque

class UnionFind(object):
    def __init__(self, nums):
        self.parent = {}
        for n in nums:
            self.parent[n] = n
        self.mp = defaultdict(list)

    def find(self, i):
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]] # path compression
            i = self.parent[i]
        return i

    def union(self, i, j):
        pj = self.find(j)
        self.parent[self.find(i)] = pj

        # add i to parent[j]'s heap
        heapq.heappush(self.mp[pj], i)
    
    def get_min(self, i):
        pi = self.find(i)
        return heapq.heappop(self.mp[pi]) if self.mp[pi] else -1


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        """
        Time complexity: O(nlogn)
        Space complexity: O(n)
        """
        sorted_nums = sorted(nums)
        n = len(nums)
        uf = UnionFind(nums)
        uf.union(sorted_nums[0], sorted_nums[0])

        for i in range(1, n):
            # form a component
            if sorted_nums[i] - sorted_nums[i - 1] <= limit:
                uf.union(sorted_nums[i], sorted_nums[i - 1])
            else:
                uf.union(sorted_nums[i], sorted_nums[i])
        
        for i in range(n):
            nums[i] = uf.get_min(nums[i])

        return nums
    
    def lexicographicallySmallestArray2(self, nums: List[int], limit: int) -> List[int]:
        groups = {}
        prev = float('-inf')
        for n in sorted(nums):
            if n - prev > limit:
                g = deque()
            g.append(n)
            groups[n] = g
            prev = n

        return [groups[n].popleft() for n in nums]
            

if __name__ == '__main__':
    sol = Solution()
    nums = [1,5,3,9,8]
    limit = 2
    print(sol.lexicographicallySmallestArray(nums, limit))