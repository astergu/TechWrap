"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.

"""

import sys
import unittest


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        Time complexity: O(m * n), Space complexity: O(m)
        """
        if not coins:
            return -1
        coins.sort()
        res = [sys.maxint] * (amount + 1)
        res[0] = 0
        for i in xrange(len(coins) - 1, -1, -1):
            for j in xrange(1, amount + 1):
                if j - coins[i] >= 0:
                    res[j] = min(res[j - coins[i]] + 1, res[j])
        return res[amount] if res[amount] != sys.maxint else -1


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        coins = [1, 2, 5]
        amount = 11
        ret = self.s.coinChange(coins, amount)
        self.assertEqual(ret, 3)

    def test2(self):
        coins = [2]
        amount = 3
        ret = self.s.coinChange(coins, amount)
        self.assertEqual(ret, -1)

    def test3(self):
        coins = [186,419,83,408]
        amount = 6249
        ret = self.s.coinChange(coins, amount)
        self.assertEqual(ret, 20)


if __name__ == '__main__':
    unittest.main()
    #coins = [1, 2, 5]
    #amount = 11
    #s = Solution()
    #ret = s.coinChange(coins, amount)
    #print "ret: ", ret
