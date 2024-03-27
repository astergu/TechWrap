'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        sl = list(s)
        i, j = 0, len(s) - 1
        while i <= j:
            print("[i] {}, [j] {}".format(i, j))
            if sl[i].lower() not in vowels:
                i += 1
                continue
            if sl[j].lower() not in vowels:
                j -= 1
                continue
            sl[i], sl[j] = sl[j], sl[i]
            i += 1
            j -= 1
        
        return "".join(sl)


if __name__ == '__main__':
    sol = Solution()
    s = "aA"
    print(sol.reverseVowels(s))