'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        tc, sc = Counter(t), {}
        matched_keys = 0
        left, right, start, size = 0, 0, 0, float('inf')
        while right < len(s):
            if s[right] in tc:
                sc[s[right]] = sc.get(s[right], 0) + 1
                if sc[s[right]] == tc[s[right]]:
                    matched_keys += 1
            right += 1 # expand right window

            while matched_keys == len(tc): # ok to shrink left window
                if right - left < size:
                    start = left
                    size = right - left
                
                if s[left] in tc:
                    sc[s[left]] -= 1
                    if sc[s[left]] < tc[s[left]]:
                        matched_keys -= 1
                left += 1
        
        return s[start:start + size] if size != float('inf') else ""


if __name__ == '__main__':
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.minWindow(s, t))