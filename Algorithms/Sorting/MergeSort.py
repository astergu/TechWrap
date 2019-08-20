# coding=utf8

import sys


class Solution:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        left, right = self.split(arr)
        return self.merge(self.merge_sort(left), self.merge_sort(right))

    def split(self, arr):
        middle = len(arr) // 2
        return arr[:middle], arr[middle:]

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        ret = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1
        if i < len(left):
            ret += left[i:]
        if j < len(right):
            ret += right[j:]
        return ret


if __name__ == '__main__':
    s = Solution()
    arr = [1, 3, 9, 6, 5, 2]
    print(s.merge_sort(arr))
