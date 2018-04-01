"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

import unittest


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, last = 0, -1  # last: the last position of )
        stack = []             # the positions of non-matching (
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if not stack:
                    last = i
                else:
                    stack.pop()
                    if not stack:
                        longest = max(longest, i - last)
                    else:
                        longest = max(longest, i - stack[-1])
        return longest

    # Dynamic Programming, One Pass
    # Time O(n), Space O(n)

    # Two-way scan
    # Time O(n), Space O(1)


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        string = ")()())"
        self.assertEqual(self.s.longestValidParentheses(string), 4)

    def test2(self):
        string = ")()())(((((()()()()("
        self.assertEqual(self.s.longestValidParentheses(string), 8)

    def test3(self):
        string = "()(())"
        self.assertEqual(self.s.longestValidParentheses(string), 6)


if __name__ == '__main__':
    unittest.main()