#coding=utf8

"""
Given a string, print all permutations of a given string.

Input:

The first line of input contains an integer T denoting the number of test cases.
Each test case contains a single string in capital letter.

Output:

Print all permutations of a given string with single space and all permutations should be in lexicographically increasing order.

"""

import unittest


class Solution(object):
    def permutations(self, s):
        ret = [[]]
        for char in s:
            nret = []
            for perm in ret:
                for j in xrange(len(perm) + 1):
                    nret.append(perm[j:] + [char] + perm[:j])
            ret = nret
        return [''.join(item) for item in ret]

    def permutations_str(self, s):
        for i, char in enumerate(s):
            pass

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        str = "ABC"
        output = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
        self.assertListEqual(self.s.permutations(str), output)

    def test2(self):
        str = "AAB"
        output = ["AAB", "ABA", "BAA"]
        self.assertListEqual(self.s.permutations(str), output)


if __name__ == '__main__':
    #unittest.main()
    str = "ABC"
    str2 = "AAB"
    s = Solution()
    print s.permutations(str)
    #print s.permutations(str2)