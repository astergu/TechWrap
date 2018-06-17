"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

from math import sqrt, floor
import sys

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.numSquares_dp(n)

    def numSquares_dp(self, n):
        dp = [sys.maxint] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in xrange(2, n + 1):
            for j in xrange(int(floor(sqrt(i))), 0, -1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]


if __name__ == '__main__':
    n = 12
    s = Solution()
    ret = s.numSquares(n)
    print ret
