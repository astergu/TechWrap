'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1. 
'''



class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        res = [0] * (n + 1)
        for i in range(n + 1):
            if i == 1:
                res[i] = 1
            else:
                res[i] = res[i - 1] + res[i - 2]
        
        return res[n]


if __name__ == '__main__':
    sol = Solution()
    n = 0
    print(sol.fib(n))