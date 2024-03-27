'''
Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.

Note:

A lattice point is a point with integer coordinates.
Points that lie on the circumference of a circle are also considered to be inside it.
'''

from typing import List

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        pass


if __name__ == '__main__':
    sol = Solution()
    circles = [[2,2,1]]
    print(sol.countLatticePoints(circles))