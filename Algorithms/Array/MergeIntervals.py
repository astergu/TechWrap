"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        ans = []
        start, end = intervals[0].start, intervals[0].end
        for i in xrange(1, len(intervals)):
            if intervals[i].start <= end:
                start = min(intervals[i].start, start)
                end = max(intervals[i].end, end)
            else:
                ans.append(Interval(start, end))
                start, end = intervals[i].start, intervals[i].end

        ans.append(Interval(start, end))
        return ans


if __name__ == '__main__':
    s = Solution()
    intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    ret = s.merge(intervals)
    print ret
