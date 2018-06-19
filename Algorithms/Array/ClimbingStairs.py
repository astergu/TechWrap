#coding=utf8

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

import unittest


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        ways = [0] * (n + 1)
        ways[0] = ways[1] = 1
        for i in xrange(2, n + 1):
            ways[i] = ways[i - 2] + ways[i - 1]
        return ways[n]


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        n = 3
        self.assertEqual(self.s.climbStairs(n), 3)

    def test2(self):
        n = 2
        self.assertEqual(self.s.climbStairs(n), 2)

    def test3(self):
        n = 4
        self.assertEqual(self.s.climbStairs(n), 5)

if __name__ == '__main__':
    unittest.main()
