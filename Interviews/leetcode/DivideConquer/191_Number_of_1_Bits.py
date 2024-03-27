'''
Write a function that takes the binary representation of a positive integer and returns the number of
set bits
it has (also known as the Hamming weight).

 

Example 1:

Input: n = 11

Output: 3

Explanation:

The input binary string 1011 has a total of three set bits.

Example 2:

Input: n = 128

Output: 1

Explanation:

The input binary string 10000000 has a total of one set bit.

'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
            #print(n, ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 2147483645
    print(sol.hammingWeight(n))