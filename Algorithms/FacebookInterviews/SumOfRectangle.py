#!/usr/bin/env python

"""
Suppose you have a matrix of numbers. How can you easily compute the sum of any rectangle (i.e. a range [row_start, row_end, col_start, col_end]) of these numbers? How would you code this?

Possible questions to ask:
1. Will the index always be valid?
2. How is the row and col indexed? Start from 0 or 1?
"""

import unittest

def computeRectangleSum(matrix, row_start, row_end, col_start, col_end):
    total = 0
    for i in xrange(row_start, row_end + 1):
        total += sum([matrix[i][x] for x in xrange(col_start, col_end + 1)])
    return total


class SolutionTest(unittest.TestCase):
    def test1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        row_start, row_end = 1, 2
        col_start, col_end = 1, 2
        ret = computeRectangleSum(matrix, row_start, row_end, col_start, col_end)
        self.assertEqual(ret, 28)


if __name__ == '__main__':
    unittest.main()
