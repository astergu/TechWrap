'''
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

'''

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            t = temperatures[i]
            while stack:
                if stack[-1][1] > t:
                    break
                stack.pop()
            ans[i] = stack[-1][0] - i if stack else 0
            stack.append((i, t)) 
            print("[i] {}, [temp] {}, [stack] {}, [ans] {}".format(i, t, stack, ans))
        
        return ans


if __name__ == '__main__':
    sol = Solution()
    temperatures = [30, 40, 50, 60]
    print(sol.dailyTemperatures(temperatures))