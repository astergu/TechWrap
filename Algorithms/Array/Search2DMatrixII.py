class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            if matrix[i][0] <= target:
                res = self.binary_search(target, matrix[i])
                if res:
                    return True
        return False

    def binary_search(self, target, lst):
        low, high = 0, len(lst) - 1
        while low <= high:
            mid = (low + high) / 2
            if target == lst[mid]:
                return True
            elif target < lst[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False


if __name__ == '__main__':
    input = [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ]
    s = Solution()
    print s.searchMatrix(input, 20)
