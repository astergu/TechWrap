#coding=utf8

"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""


import unittest


class Solution(object):
    def naive_findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        Time Complexity: ?
        Time limit exceeded.
        """
        from collections import Counter
        ret = []
        m, lenp, cntp = 0, len(p), Counter(p)
        while m < len(s) and m + len(p) <= len(s):
            if Counter(s[m:m+len(p)]) == cntp:
                ret.append(m)
            m += 1
        return ret

    def findAnagram(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]

        """
        if len(s) < len(p):
            return []

        from collections import Counter
        cntp = Counter(p)  # 目标串的字符构成
        start, end = 0, 0  # 双指针记录起止位置
        cnt = len(cntp.keys())  # 目标串的不重复字符个数
        ret = []

        while end < len(s):  # 终止条件：end指针超出搜寻串长度
            curr = s[end]
            if curr in cntp:  # 如果当前字符在目标串里
                cntp[curr] = cntp[curr] - 1  # 对目标串的该字符个数减1
                if cntp[curr] == 0:  # 如果该字符在目标串中的出现次数已经全部满足，则字符count减1
                    cnt -= 1
            end += 1

            while cnt == 0:  # 如果目标串的字符匹配全部满足，即找到目标串的anagrams
                curr = s[start]
                if curr in cntp: # 如果当前字符在目标串里
                    cntp[curr] = cntp[curr] + 1  # 窗口向后挪一个，当前字符在window串口里的待搜寻个数就加1
                    if cntp[curr] > 0: # 如果在目标串中当前字符个数大于0，则递增
                        cnt += 1

                if end - start == len(p):
                    ret.append(start)
                start += 1
        return ret


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        s = "cbaebabacd"
        p = "abc"
        output = [0, 6]
        self.assertListEqual(self.s.findAnagram(s, p), output)

    def test2(self):
        s = "abab"
        p = "ab"
        output = [0, 1, 2]
        self.assertListEqual(self.s.findAnagram(s, p), output)


if __name__ == '__main__':
    unittest.main()