'''
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:

Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
'''
from typing import List
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = dict(sorted(Counter(arr).items(), key=lambda x: x[1]))
        uniq = len(cnt)
        for n, v in cnt.items():
            if k <= 0 or k < v:
                return uniq
            k -= v
            uniq -= 1
        
        return uniq


if __name__ == '__main__':
    sol = Solution()
    arr = [4,3,1,1,3,3,2]
    k = 3
    print(sol.findLeastNumOfUniqueInts(arr, k))