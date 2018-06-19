"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2

Example 2:

Input: " 2-1 + 2 "
Output: 3

Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:

    You may assume that the given expression is always valid.
    Do not use the eval built-in library function.


"""

import unittest


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        tokens = self.toRPN(s)
        return self.evalRPN(tokens)

    operators = ['+', '-', '*', '/']

    def toRPN(self, s):
        tokens, stack = [], []
        number = ''
        for c in s:
            if c.isdigit():
                number += c
            else:
                if number:
                    tokens.append(number)
                    number = ''
                if c in self.operators:
                    while len(stack):
                        tokens.append(stack.pop())
                    stack.append(c)
                elif c == '(':
                    stack.append(c)
                elif c == ')':
                    while len(stack) and stack[-1] != '(':
                        tokens.append(stack.pop())
                    stack.pop()
            if number:
                tokens.append(number)
            while len(stack):
                tokens.append(stack.pop())
            return tokens

    def evalRPN(self, tokens):
        operands = []
        for token in tokens:
            if token in self.operators:
                y, x = operands.pop(), operands.pop()
                operands.append(self.getVal(x, y, token))
            else:
                operands.append(int(token))
        return operands[0]

    def getVal(self, x, y, operator):
        return {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                }[operator](x, y)


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        input = "1 + 1"
        output = 2
        ret = self.s.calculate(input)
        self.assertEqual(ret, output)


if __name__ == '__main__':
    #unittest.main()
    s = Solution()
    #input = " 2-1 + 2 "
    #input = "(1+(4+5+2)-3)+(6+8)"
    input = "2147483647"
    print input
    print
    output = s.calculate(input)
    print output
