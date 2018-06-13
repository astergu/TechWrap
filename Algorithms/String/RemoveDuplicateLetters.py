"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

    Input: "bcabc"
    Output: "abc"

Example 2:

    Input: "cbacdcbc"
    Output: "acdb"

"""


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for x in range(len(set(s))):
            top, idx = s[0], 0
            counter = collections.Counter(s)
            for y in range(len(s)):
                if top > s[y]:
                    top, idx = s[y], y
                if counter[s[y]] == 1:
                    break
                counter[s[y]] -= 1
            ans += top
            s = s[idx+1:].replace(top,'')
        return ans

    def removeDuplicateLettersStack(self, s):
        counter = collections.Counter(s)
        resultSet = set()
        stack = list()
        for c in s:
            counter[c] -= 1
            if c in resultSet:
                continue
            while stack and stack[-1] > c and counter[stack[-1]]:
                resultSet.remove(stack.pop())
            resultSet.add(c)
            stack.append(c)
        return ''.join(stack)

    def removeDuplicateLettersRecursive(self, s):
        for c in sorted(set(s)):
        suffix = s[s.index(c):]
        if set(suffix) == set(s):
            return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''

if __name__ == '__main__':
    s = Solution()
    #input = "cbacdcbc"
    #input = "bcabc"
    #input = "bbcaac"
    #input = "ccacbaba"
    #input = "thesqtitxyetpxloeevdeqifkz"
    #input = "cbac"
    #input = "bbcaac"
    #input = "abacb"
    input = "bbcab"
    ret = s.removeDuplicateLetters(input)
    print ret
