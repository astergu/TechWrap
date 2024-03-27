'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Solution: 
        如何判断palindrome：
        1. 单个字符：Yes
        2. 多个字符，前后字母一样
        """
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        ans = 0

        for l in range(1, n + 1):
            for i in range(n - l + 1):
                if s[i] == s[i + l - 1] and (l <= 2 or palindrome[i+1][i+l-2]):
                    palindrome[i][i+l-1] = True
                    ans += 1

        print(palindrome)
        return ans


if __name__ == '__main__':
    sol = Solution()
    s = "abc"
    print(sol.countSubstrings(s))