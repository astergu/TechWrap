'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

'''

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        while asteroids:
            pass       
        """
        while len(asteroids) >= 2:
            a1, a2 = asteroids.pop(), asteroids.pop()
            if a1 == -a2:
                continue
            sign = a1 * a2
            if sign < 0: 
                val = a1 if abs(a1) > abs(a2) else a2
                stack.append(val)
            else:
                stack.append((a1, a2)) 

            print(a1, a2, stack, asteroids) 
        """


if __name__ == '__main__':
    sol = Solution()
    asteroids = [8, -8]
    print(sol.asteroidCollision(asteroids))