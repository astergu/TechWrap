'''
You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

    For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.

Equivalent characters follow the usual rules of any equivalence relation:

    Reflexivity: 'a' == 'a'.
    Symmetry: 'a' == 'b' implies 'b' == 'a'.
    Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.

For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
'''

import string

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = list(range(26))
        A = ord('a')
        
        def find(c):
            i = ord(c) - A
            while root[i] != i:
                i = root[i]
            return i

        for c1, c2 in zip(s1, s2):
            r1, r2 = find(c1), find(c2)
            if r1 > r2:
                r1, r2 = r2, r1
            root[r2] = r1

        return ''.join(chr(A + find(c)) for c in baseStr) 


if __name__ == '__main__':
    sol = Solution()
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    print(sol.smallestEquivalentString(s1, s2, baseStr))