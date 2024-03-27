'''
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.


Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res, d = 0, n
        while d // 5 > 0:
            res += d // 5
            d = d // 5
        return res

    def trailingZeroes2(self, n: int) -> int:
        if n == 0:
            return 0
        return n // 5 + self.trailingZeroes2(n // 5)

if __name__ == '__main__':
    sol = Solution()
    n = 25
    print(sol.trailingZeroes(n))