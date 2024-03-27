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
        vowels = ["a", "e", "i", "o", "u"]
        max_num, vowel_num = 0, 0
        i, j = 0, 0
        while i < len(s):
            if s[i] in vowels:
                vowel_num += 1
            if i + j - 1 == k:
                max_num = max(max_num, vowel_num)
                if s[j] in vowels:
                    vowel_num -= 1
                j += 1
            
            if max_num == k:
                return k
        
        return max_num


if __name__ == '__main__':
    sol = Solution()
    s = "abciiidef"
    k = 3
    print(sol.maxVowels(s, k))