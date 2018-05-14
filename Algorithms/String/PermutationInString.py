#coding=utf8

"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:

    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].

"""

import unittest


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        from collections import Counter
        count_dict = Counter(s1)
        start, end, counter = 0, 0, len(count_dict)
        while end < len(s2):
            curr = s2[end]
            if curr in count_dict:
                count_dict[curr] = count_dict[curr] - 1
                if count_dict[curr] == 0:
                    counter -= 1
            end += 1

            while counter == 0:
                curr = s2[start]
                if curr in count_dict:
                    count_dict[curr] = count_dict[curr] + 1
                    if count_dict[curr] > 0:
                        counter += 1
                if end - start == len(s1):
                    return True
                start += 1
        return False


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    """
    def test1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        self.assertEqual(self.s.checkInclusion(s1, s2), True)

    def test2(self):
        s1 = "ab"
        s2 = "eidaoaoo"
        self.assertEqual(self.s.checkInclusion(s1, s2), False)

    def test3(self):
        s1 = "hello"
        s2 = "ooolleoooleh"
        self.assertEqual(self.s.checkInclusion(s1, s2), False)
    """

    def test4(self):
        s1 = "adc"
        s2 = "dcda"
        self.assertEqual(self.s.checkInclusion(s1, s2), True)


if __name__ == '__main__':
    unittest.main()