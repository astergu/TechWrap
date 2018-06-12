"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
    Given s = "hello", return "holle".

Example 2:
    Given s = "leetcode", return "leotcede".

Note:
    The vowels does not include the letter "y".
"""

import sys


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            left_lt, right_lt = s[left].lower(), s[right].lower()
            if left_lt not in vowels:
                left += 1
            if right_lt not in vowels:
                right -= 1
            if left_lt in vowels and right_lt in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)


if __name__ == '__main__':
    sol = Solution()
    #s = "leetcode"
    s = "aA"
    ret = sol.reverseVowels(s)
    print ret
