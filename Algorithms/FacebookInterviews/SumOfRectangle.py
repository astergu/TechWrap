#!/usr/bin/env python

"""
Suppose you have a matrix of numbers. How can you easily compute the sum of any rectangle (i.e. a range [row_start, row_end, col_start, col_end]) of these numbers? How would you code this?

The key concern: [frequent query] on a [static matrix], so this is a DP problem.

Possible questions to ask:
1. Will the index always be valid?
2. How is the row and col indexed? Start from 0 or 1?
"""

import unittest


class MatrixRectangle(object):
    def __init__(self, matrix):
        if not matrix:
            print "Matrix is empty!"
        self._matrix = matrix
        self.calculate_rectangle()

    def is_empty(self):
        if self._matrix:
            return False
        return True

    def calculate_rectangle(self):
        self._area = [[0] * len(self._matrix[0]) for x in xrange(len(self._matrix))]
        self._area[0][0] = self._matrix[0][0]

        for i in xrange(1, len(self._matrix)):
            self._area[i][0] = self._area[i-1][0] + self._matrix[i][0]
        for j in xrange(1, len(self._matrix[0])):
            self._area[0][j] = self._area[0][j-1] + self._matrix[0][j]

        for i in xrange(1, len(self._matrix)):
            for j in xrange(1, len(self._matrix[0])):
                self._area[i][j] = self._area[i][j-1] + self._area[i-1][j] \
                                       - self._area[i-1][j-1] + self._matrix[i][j]

    def computeRectangleSum(self, row_start, row_end, col_start, col_end):
        row_low, col_low = max(row_start - 1, 0), max(col_start - 1, 0)
        return self._area[row_end][col_end] + self._area[row_low][col_low] \
                - self._area[row_end][col_low] - self._area[row_low][col_end]


class SolutionTest(unittest.TestCase):
    def setUp(self):
        matrix = [[1, 2, 3, 7], [4, 5, 6, 1], [7, 8, 9, 2]]
        self.cls = MatrixRectangle(matrix)

    def test1(self):
        row_start, row_end = 1, 2
        col_start, col_end = 1, 2
        ret = self.cls.computeRectangleSum(row_start, row_end, col_start, col_end)
        self.assertEqual(ret, 28)

    def test2(self):
        row_start, row_end = 0, 1
        col_start, col_end = 0, 1
        ret = self.cls.computeRectangleSum(row_start, row_end, col_start, col_end)
        self.assertEqual(ret, 5)

if __name__ == '__main__':
    unittest.main()
