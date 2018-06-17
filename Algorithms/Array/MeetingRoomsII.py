"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

import collections
import heapq

# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        return self.minMeetingRooms_heap(intervals)

    def minMeetingRooms_heap(self, intervals):
        points = collections.defaultdict(list)
        for inter in intervals:
            points[inter.start].append(inter)
            points[inter.end].append(inter)

        current_meeting = []
        max_meetings = 0
        for point in sorted(list(points.keys()), key=lambda x: x):
            meetings = points[point]
            for meeting in meetings:
                if point == meeting.start:
                    heapq.heappush(current_meeting, meeting.start)
                elif point == meeting.end:
                    current_meeting.remove(meeting.start)
                    heapq.heapify(current_meeting)
            max_meetings = max(max_meetings, len(current_meeting))
        return max_meetings


    def minMeetingRooms_scan(self, intervals):
        if not intervals or len(intervals) == 0:
            return 0
        tmp = []
        for inter in intervals:
            tmp.append((inter.start, True))
            tmp.append((inter.end, False))

        tmp = sorted(tmp, key=lambda v: (v[0], v[1]))

        n = 0
        max_num = 0
        for arr in tmp:
            if arr[1]: # start
                n += 1
            else:
                n -= 1
            max_num = max(n, max_num)
        return max_num



if __name__ == '__main__':
    intervals = [Interval(7, 10), Interval(2, 4)]
    s = Solution()
    ret = s.minMeetingRooms(intervals)
    print ret
