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

import unittest


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        coins.sort()
        count, idx = 0, len(coins) - 1
        while amount > 0 and idx >= 0:
            print "amount: ", amount, ", idx: ", idx, ", count: ", count
            divisor = amount / coins[idx]
            amount -= coins[idx] * divisor
            count += divisor
            idx -= 1

        return count if amount == 0 else -1


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    """
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
    """

    def test3(self):
        coins = [186,419,83,408]
        amount = 6249
        ret = self.s.coinChange(coins, amount)
        self.assertEqual(ret, 20)

if __name__ == '__main__':
    unittest.main()
