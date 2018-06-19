"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(s) + 1)] for j in range(len(p) + 1)]
        dp[0][0] = True
        for i in xrange(1, len(p) + 1):
            if dp[i-1][0] == True and p[i-1] == '*':
                dp[i][0] = True
        for i in xrange(1, len(p) + 1):
            for j in xrange(1, len(s) + 1):
                if p[i-1] == s[j-1] or p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j-1] | dp[i][j-1] | dp[i-1][j]
        return dp[len(p)][len(s)]

if __name__ == '__main__':
    s = "adceb"
    p = "*a*b"
    sol = Solution()
    print sol.isMatch(s, p)
