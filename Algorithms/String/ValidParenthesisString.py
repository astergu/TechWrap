"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
"""

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lower, upper = 0, 0
        for c in s:
            if c == '(':
                lower += 1
                upper += 1
            elif c == ')':
                low -= 1
                upper -= 1
            else:  # * encountered
                lower -= 1
                upper += 1
            lower = max(lower, 0)
            if upper < 0:
                return False
        return lower == 0
