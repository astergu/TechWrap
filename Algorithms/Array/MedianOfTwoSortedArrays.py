#coding=utf8

"""
4.

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

import unittest


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total >> 1
        if total & 0x1: # odd number
            return self.findKth(nums1, m, nums2, n, half + 1)
        else:
            return (self.findKth(nums1, m, nums2, n, half) +
                    self.findKth(nums1, m, nums2, n, half + 1)) / 2.0

    def findKth(self, A, m, B, n, k):
        if m > n:
            return self.findKth(B, n, A, m, k)
        if m == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])

        ia = min(k / 2, m)
        ib = k - ia
        if A[ia - 1] > B[ib - 1]:
            return self.findKth(A, m, B[ib:], n - ib, k - ib)
        elif A[ia - 1] < B[ib - 1]:
            return self.findKth(A[ia:], m - ia, B, n, k - ia)
        else:
            return A[ia - 1]


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        nums1 = [1, 3]
        nums2 = [2]
        ret = self.s.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(ret, 2)

    #def test2(self):
    #    nums1 = [1, 2]
    #    nums2 = [3, 4]
    #    ret = self.s.findMedianSortedArrays(nums1, nums2)
    #    self.assertEqual(ret, 2.5)


if __name__ == '__main__':
    unittest.main()
