"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        memo = dict()
        def dfs(s):
            ans = []
            if s in wordDict:
                ans.append(s)
            for x in range(len(s) - 1):
                prefix, suffix = s[:x+1], s[x+1:]
                if prefix not in wordDict:
                    continue
                rest = []
                if suffix in memo:
                    rest = memo[suffix]
                else:
                    rest = dfs(suffix)
                for n in rest:
                    ans.append(prefix + ' ' + n)
            memo[s] = ans
            return ans

        return dfs(s)


if __name__ == '__main__':
    sol = Solution()
    #s = "catsanddog"
    s = "a"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    output = sol.wordBreak(s, wordDict)
    print output
