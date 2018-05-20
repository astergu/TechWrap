#coding=utf8

"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""

import unittest


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        ct = Counter(s)
        odds = 0
        for k, v in ct.items():
            odds += v & 1
        return len(s) - odds + (odds > 0)


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        input = "abccccdd"
        output = 7
        self.assertEqual(self.s.longestPalindrome(input), output)


if __name__ == '__main__':
    unittest.main()