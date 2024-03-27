'''
Given an integer n, return the number of prime numbers that are strictly less than n.
'''

import sys

class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Sieve of Eratosthenes
        Time Complexity: O(N * loglogN)
        """
        isPrime = [True] * n
        i = 2
        while i * i < n:
            if self.isPrime(i):
                for j in range(i * i, n, i):
                    isPrime[j] = False
            i += 1
        
        return isPrime[2:].count(True) 
    
    def isPrime(self, n):
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


if __name__ == '__main__':
    sol = Solution()
    n = 10
    print(sol.countPrimes(n)) 