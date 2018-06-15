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
        stack = []
        for c in s:
            print "%s" % c,
            print stack
            if c == ' ':
                continue
            if c in ['+', '-', '(']:
                stack.append(c)
            elif c.isdigit():
                if not stack or stack[-1] not in ['+', '-']:
                    stack.append(c)
                elif stack[-1] in ['+', '-']:
                    op = stack.pop()
                    lvalue = stack.pop()
                    res = self.apply_op(op, lvalue, c)
                    stack.append(res)
            elif c == ')':
                last = stack.pop()
                lvalue = stack.pop()
                res = None
                while lvalue != '(':
                    left = stack.pop()
                    last = self.apply_op(lvalue, left, last)
                    lvalue = stack.pop()
                stack.append(last)


        #print "____________ STACK _____________"
        #print stack

        while stack and len(stack) > 1:
            right = stack.pop()
            op = stack.pop()
            left = stack.pop()
            res = self.apply_op(op, left, right)
            stack.append(res)

        return stack[-1]


    def apply_op(self, op, lv, rv):
        if op == '+':
            return int(lv) + int(rv)
        if op == '-':
            return int(lv) - int(rv)


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
