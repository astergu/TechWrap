# coding=utf8

import sys


class Solution:
    def merge_sort(self, arr):
        if len(arr) == 1:
            return arr[0]
        pivot = len(arr) << 1
        left = self.merge_sort(arr[:pivot])
        right = self.merge_sort(arr[pivot:])
        ret = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1
        while i < len(left):
            ret.append(left[i])
            i += 1
        while j < len(right):
            ret.append(right[i])
            j += 1
        return ret


if __name__ == '__main__':
    s = Solution()
    arr = [1, 3, 9, 6, 5, 2]
    print(s.merge_sort(arr))
