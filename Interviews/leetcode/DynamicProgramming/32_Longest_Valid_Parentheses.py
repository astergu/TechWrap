'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0

'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            pass


if __name__ == '__main__':
    sol = Solution()
    s = "(())"
    print(sol.longestValidParentheses(s))