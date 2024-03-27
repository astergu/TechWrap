'''
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
'''

from typing import List
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit)) 
        print(jobs)
        n = len(profit)
        dp = [0] * (n + 1)
      
        for i, (e, s, p) in enumerate(jobs):
            idx = bisect_right(jobs, s, hi=i, key=lambda x: x[0]) # find the closest job that finished before the current job's start time
            dp[i + 1] = max(dp[i], dp[idx] + p)
            print("[start] {}, [end] {}, [profit] {}, [index] {}, [dp] {}".format(s, e, p, idx, dp))
      
        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    startTime = [1,2,3,3]
    endTime = [3,4,5,6]
    profit = [50,10,40,70]
    print(sol.jobScheduling(startTime, endTime, profit))