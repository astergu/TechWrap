'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        cur_v = max_v = sum([1 for x in s[:k] if x in vowels])
        print(cur_v, max_v)
        for i in range(0, len(s) - k):
            cur_v += (s[i + k] in vowels) - (s[i] in vowels)
            if cur_v > max_v:
                max_v = cur_v

        return max_v 


if __name__ == '__main__':
    sol = Solution()
    s = "abciiidef"
    k = 3
    print(sol.maxVowels(s, k))