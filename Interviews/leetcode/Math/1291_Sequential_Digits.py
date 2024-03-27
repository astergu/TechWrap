'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

'''

from typing import List
from collections import deque

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        Time: O(9loghigh) = O(loghigh)
        Space: O(loghigh)
        """
        ans = []
        q = deque([num for num in range(1, 10)])

        while q:
            n = q.popleft()
            if n > high:
                return ans
            if low <= n and n <= high:
                ans.append(n)
            last_digit = n % 10
            if last_digit < 9:
                q.append(n * 10 + last_digit + 1)
            print('[num]: ', n, ", [q]: ", q)

        return ans 


if __name__ == '__main__':
    sol = Solution()
    low = 100
    high = 300
    print(sol.sequentialDigits(low, high))