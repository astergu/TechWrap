class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[""] * len(s) for _ in range(len(s))]
        for k in xrange(len(s)):
            for i in xrange(len(s) - k):  # i + k <= len(s)
                j = i + k
                substr = s[i:j+1]
                if j - i < 4:
                    dp[i][j] = substr  # < 5, no need to encode
                else:
                    dp[i][j] = substr
                    for m in xrange(i, j):
                        if len(dp[i][m] + dp[m + 1][j]) < len(dp[i][j]):
                            dp[i][j] = dp[i][m] + dp[m + 1][j]

                    for n in xrange(len(substr)):
                        repeatStr = substr[:n+1]
                        if repeatStr and len(substr.replace(repeatStr, "")) == 0:
                            count = len(substr) / len(repeatStr)
                            ss = str(count) + "[" + dp[i][i+n] + "]"
                            if len(ss) < len(dp[i][j]):
                                dp[i][j] = ss

        return dp[0][len(s) - 1]


if __name__ == '__main__':
    input = "aaaaa"
    s = Solution()
    output = s.encode(input)
    print output
