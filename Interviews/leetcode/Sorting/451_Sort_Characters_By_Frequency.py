'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        freq = sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
        return "".join([x[0] * x[1] for x in freq])

if __name__ == '__main__':
    sol = Solution()
    s = "tree"
    print(sol.frequencySort(s))