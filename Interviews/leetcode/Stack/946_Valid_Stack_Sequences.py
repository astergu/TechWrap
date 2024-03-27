'''
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

'''

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack =[]
        x = 0
        for i in pushed:
            stack.append(i)
            if len(stack) > 0 and stack[len(stack)-1] == popped[x]:
                while len(stack) > 0 and stack[len(stack)-1] == popped[x]:
                    x += 1
                    stack.pop()
        return len(stack) == 0


if __name__ == '__main__':
    sol = Solution()
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    print(sol.validateStackSequences(pushed, popped))