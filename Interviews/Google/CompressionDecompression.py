"""
In this exercise, you're going to decompress a compressed string.

Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

The input

3[abc]4[ab]c

Would be output as

abcabcabcababababc

Other rules
Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

Characters allowed as input include digits, small English letters and brackets [ ].

Digits are only to represent amount of repetitions.

Letters are just letters.

Brackets are only part of syntax of writing repeated substring.

Input is always valid, so no need to check its validity.


Edge cases:
    a[]b, 0[abc]
"""

import unittest


def decomp(s, start=0, times=0):
    ret = ""
    i = start
    if i < len(s):
        while i < len(s):
            print "i: ", i, ", times: ", times
            if s[i].isdigit():
                times = times * 10 + int(s[i])
            elif s[i] == '[':
                ret += decomp(s, i + 1, times)
            elif s[i] == ']':
                print "start: ", start, ", s[start:i]: ", s[start:i]
                temp = s[start:i] * times
                print "temp: ", temp
                return temp
            i += 1
    return ret


def decompress(s):
    return decomp(s)


class SolutionTest(unittest.TestCase):
    def test1(self):
        s = "3[abc]4[ab]c"
        ret = decompress(s)
        self.assertEqual(ret, "abcabcabcababababc")

    def test2(self):
        s = "2[3[a]b]"
        truth = "aaabaaab"
        ret = decompress(s)
        self.assertEqual(ret, truth)


if __name__ == '__main__':
    #unittest.main()
    s = "3[abc]4[ab]c"
    #s = "2[3[a]b]"
    ret = decompress(s)
    print ret

