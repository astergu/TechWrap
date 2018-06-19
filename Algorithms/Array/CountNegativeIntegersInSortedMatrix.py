class Solution(object):
    def numNegativeIntegers(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        count = 0
        while j >= 0 and i < m:
            if matrix[i][j] < 0:
                count += (j + 1)
                i += 1
            else:
                j -= 1
        return count


if __name__ == '__main__':
    input = [[-3, -2, -1, 1], [-2, 2, 3, 4], [4, 5, 7, 8]]
    s = Solution()
    output = s.numNegativeIntegers(input)
    print output
