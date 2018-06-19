#coding=utf8

"""
 Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

import unittest


class Solution(object):
    def trap(self, height):
        """
        :param height: List[int]
        :return: int
        """
        a, b = 0, len(height) - 1
        ret = 0
        left_max, right_max = 0, 0
        while a <= b:
            left_max = max(left_max, height[a])
            right_max = max(right_max, height[b])
            if left_max < right_max:
                ret += (left_max - height[a])
                a += 1
            else:
                ret += (right_max - height[b])
                b -= 1
        return ret

    def trap2(self, height):
        n = len(height)
        left_max, right_max = [0] * n, [0] * n
        for i in xrange(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])
            right_max[n - 1 - i] = max(right_max[n - i], height[n - i])

        area = 0
        for i in xrange(n):
            h = min(left_max[i], right_max[i])
            if h > height[i]:
                area += h - height[i]

        return area


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(self.s.trap2(height), 6)


if __name__ == '__main__':
    unittest.main()