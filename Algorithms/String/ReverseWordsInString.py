#coding=utf8

"""
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".

Note:

    A word is defined as a sequence of non-space characters.
    Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
    You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up: For C programmers, try to solve it in-place in O(1) space.

"""

import unittest


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        str = "hello"
        output = "hello"
        self.assertEqual(self.s.reverseWords(str), output)

    def test2(self):
        str = " abc def    "
        output = "def abc"
        self.assertEqual(self.s.reverseWords(str), output)


if __name__ == '__main__':
    unittest.main()