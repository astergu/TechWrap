class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        parts = input.split('\n')
        stack = [(-1, 0)]
        ans = length = 0
        for part in parts:
            depth = part.count('\t')
            name = part.replace('\t', '')
            top_depth, top_length = stack[-1]  # last depth and length
            while depth <= top_depth:
                stack.pop()
                length -= top_length
                top_depth, top_length = stack[-1]
            sub_length = len(name) + (depth > 0)
            length += sub_length
            stack.append((depth, sub_length))
            if name.count('.'):
                ans = max(ans, length)
        return ans


if __name__ == '__main__':
    s = Solution()
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    output = s.lengthLongestPath(input)
    print output
