'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        dct = Counter(s)

        for i in range(len(s)):
            if dct.get(s[i]) == 1:
                return i

        return -1


if __name__ == '__main__':
    sol = Solution()
    s = "loveleetcode"
    print(sol.firstUniqChar(s))