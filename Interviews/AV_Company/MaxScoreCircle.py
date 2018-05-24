#coding=utf8

"""
思路：


"""

from math import sqrt

class Point(object):
    def __init__(self, x, y, score):
        self.x = x
        self.y = y
        self.score = score
        self.distance = self.x ** 2 + self.y ** 2

    #def __cmp__(self, other):
    #    return self.distance > other.distance

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + "): " + str(self.score)


class Solution(object):
    def maxScoreCircle(self, points):
        points.sort(key=lambda x: x.distance)
        last_radian_pow, curr_radian_pow = 0, 0
        score, accu_score = 0.0, 0.0
        for point in points:
            dist = point.distance
            if dist > curr_radian_pow:
                if accu_score > 1e-7:
                    score += accu_score
                    accu_score = 0.0
                    last_radian_pow = curr_radian_pow
                curr_radian_pow = dist
            accu_score += point.score

        if accu_score > 1e-7:
            score += accu_score
            last_radian_pow = curr_radian_pow
        return sqrt(last_radian_pow)

    def maxScoreCircle2(self, points):
        points.sort(key=lambda x: x.distance)
        score = 0
        scores = {}
        for pt in points:
            score += pt.score
            scores[pt.distance] = score
        return max(map(lambda x: x[1], scores.items()))

if __name__ == '__main__':
    s = Solution()
    pa = Point(1, 2, 3.4)
    pb = Point(-1, 3, 5.6)
    pc = Point(0, 5, 2.1)
    points = [pa, pb, pc]
    print "radian: ", s.maxScoreCircle(points)

