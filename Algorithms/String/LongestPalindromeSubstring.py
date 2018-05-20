#coding=utf8

"""
Given a string S, find the longest palindromic substring in S.

Substring of string S:

S[ i . . . . j ] where 0 ≤ i ≤ j < len(S)

Palindrome string:

A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.

Incase of conflict, return the substring which occurs first ( with the least starting index ).

Input:

The first line of input consists number of the test cases. The following T lines consist of a string each.


Output:

In each separate line print the longest palindrome of the string given in the respective test case.

Constraints:

1 ≤T≤ 100
1 ≤ str≤ 100

Example:

Input:

1
aaaabbaa

Output:

aabbaa
"""

import unittest


def longest_palindrome(s):
    """
    Dynamic Programming: Time O(n ^ 2), Space O(n)
    """
    n = len(s)
    palindrome = [[False] * n for x in xrange(n)]
    start, end = 0, 0
    for i in xrange(n):
        palindrome[i][i] = True
        for j in xrange(i):
            palindrome[j][i] = (s[j] == s[i] and (palindrome[j + 1][i - 1] or i - j < 2))
            if palindrome[j][i] and i - j > end - start:
                start, end = j, i
    return s[start:end + 1]

def


class SolutionTest(unittest.TestCase):
    def test1(self):
        input = "babad"
        output = "bab"
        self.assertEqual(longest_palindrome(input), output)

    def test2(self):
        input = "cbbd"
        output = "bb"
        self.assertEqual(longest_palindrome(input), output)


if __name__ == '__main__':
    unittest.main()

"""
n = int(input())
for i in range(n):
    str = input()
    print longest_palindrome(str)
"""