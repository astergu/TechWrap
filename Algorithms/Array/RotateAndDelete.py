#!/usr/bin/env python

import unittest


def rotate_and_delete(nums):
    """
    Time Complexity: O(N^2), Space Complexity: O(1)
    :param nums:
    :return:
    """
    iter = -1
    while len(nums) > 1:
        last = len(nums)
        last_element = nums[last - 1]
        for i in xrange(last - 2, -1, -1):
            nums[i + 1] = nums[i]
        nums[0] = last_element
        if abs(iter) <= len(nums):
            nums.pop(iter)
        else:
            nums.pop(0)
        iter -= 1
    return nums[0]


class SolutionTest(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 3, 4]
        self.assertEqual(rotate_and_delete(nums), 2)

    def test2(self):
        nums = [1, 2, 3, 4, 5, 6]
        self.assertEqual(rotate_and_delete(nums), 3)


if __name__ == '__main__':
    unittest.main()

