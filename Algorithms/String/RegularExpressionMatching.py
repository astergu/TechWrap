import unittest


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')

        i, j = 0, 0
        if j == len(p) - 1 or (j + 1 < len(p) and p[j + 1] != "*"):
            if not s and (len(p) >= 2 and p[1] != "*"):
                return False
            if p[j] == '.':
                return self.isMatch(s[i+1:], p[j+1:])
            elif p[j].isalpha():
                if not s:
                    return False
                return s[i] == p[j] and self.isMatch(s[i+1:], p[j+1:])
        else:
            if not s and (len(p) >= 2 and p[1] != "*"):
                return False
            while i < len(s) and (s[i] == p[j] or p[j] == '.'):
                if self.isMatch(s[i:], p[j + 2:]):
                    return True
                i += 1
            return self.isMatch(s[i:], p[j + 2:])


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        self.assertEqual(self.s.isMatch("aa", "a"), False)

    def test2(self):
        self.assertEqual(self.s.isMatch("aa", "aa"), True)

    def test3(self):
        self.assertEqual(self.s.isMatch("aaa", "aa"), False)

    def test4(self):
        self.assertEqual(self.s.isMatch("aa", "a*"), True)

    def test5(self):
        self.assertEqual(self.s.isMatch("aa", ".*"), True)

    def test6(self):
        self.assertEqual(self.s.isMatch("ab", ".*"), True)

    def test7(self):
        self.assertEqual(self.s.isMatch("aab", "c*a*b"), True)

    def test8(self):
        self.assertEqual(self.s.isMatch("ab", ".*c"), False)

    def test9(self):
        self.assertEqual(self.s.isMatch("aa", "."), False)

    def test10(self):
        self.assertEqual(self.s.isMatch("a", "ab*"), True)

    def test11(self):
        self.assertEqual(self.s.isMatch("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s"), True)

    def test12(self):
        self.assertEqual(self.s.isMatch("bb", ".bab"), False)

    def test13(self):
        self.assertEqual(self.s.isMatch("a", ".*..a*"), False)


if __name__ == '__main__':
    unittest.main()
