'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dct = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            if key in dct:
                dct[key].append(s)
            else:
                dct[key] = [s]
        
        return dct.values()


if __name__ == '__main__':
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams(strs))