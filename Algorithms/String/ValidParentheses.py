class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if c == ")" and last != "(":
                    return False
                if c == "]" and last != "[":
                    return False
                if c == "}" and last != "{":
                    return False
        if stack:
            return False
        return True
