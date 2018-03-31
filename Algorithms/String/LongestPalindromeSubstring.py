"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.



Example:

Input: "cbbd"

Output: "bb"

"""


def longestPalindrome(self, s):
    """
    Dynamic Programming: Time O(n^2), Space O(n)
    """
    n = len(s)
    palindrome = [[False] * n for x in xrange(n)]
    start, end = 0, 0
    for i in xrange(n):
        palindrome[i][i] = True
        for j in xrange(i):
            palindrome[j][i] = (s[j] == s[i] and (palindrome[j + 1][i - 1] or i - j < 2))
            if palindrome[j][i] and i - j + 1 > end - start:
                start, end = j, i
    return s[start:end + 1]
