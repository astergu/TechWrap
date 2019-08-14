"""
Given a list of scores of different students, return the average score of each student's top five scores
in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score. The average score 
is calculated using integer division.

Note:
1. 1 <= items.length <= 1000.
2. items[i].length == 2.
3. The IDs of the students is between 1 to 1000.
4. The score of the students is between 1 to 100.
"""

import heapq
from collections import defaultdict


class Solution(object):
    def highFive_1(self, items):
        ret = defaultdict(list)
        for x in items:
            ret[x[0]].append(x[1])

        sorted_ret = sorted(ret.items())
        res = []
        for k, v in sorted_ret:
            values = sorted(v, reverse=True)[:5]
            res.append((k, int(sum(values) / 5)))
        return res


if __name__ == '__main__':
    s = Solution()
    items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [
        2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]

    print(s.highFive_1(items))
