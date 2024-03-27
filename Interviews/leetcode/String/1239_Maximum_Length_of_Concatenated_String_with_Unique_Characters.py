'''
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

'''

from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        max_len = 0
        for a in arr:
            if len(set(a)) < len(a): # duplicate letters in a
                continue
            a = set(a)
            for c in dp:
                if a & c: # overlapping letters
                    continue
                dp.append(a | c)
            print("[a] {}, [dp] {}".format(a, dp))
        return max(len(a) for a in dp)



if __name__ == '__main__':
    sol = Solution()
    arr = ["un","iq","ue"]
    print(sol.maxLength(arr))