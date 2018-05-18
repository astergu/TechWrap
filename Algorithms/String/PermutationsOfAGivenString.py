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
        ret = []

        def permute(s, i):
            if i == len(s):
                ret.append(''.join(s))
            for j in xrange(i, len(s)):
                stcp = [c for c in s]
                stcp[j], stcp[i] = stcp[i], stcp[j]
                #print "stcp: ", stcp, ", i: ", i, ", j: ", j
                permute(stcp, i + 1)

        permute(s, 0)
        return ret


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        str = "ABC"
        output = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
        self.assertListEqual(self.s.permutations(str), output)


if __name__ == '__main__':
    unittest.main()