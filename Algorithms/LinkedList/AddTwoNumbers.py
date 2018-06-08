#!/usr/bin/env python

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

import unittest
from ListNode import ListNode


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        root = head = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            head.next = ListNode(val)
            head = head.next
        return root.next


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test1(self):
        l1 = ListNode(2)
        l11 = ListNode(4)
        l12 = ListNode(3)
        l1.next, l11.next = l11, l12

        l2 = ListNode(5)
        l21 = ListNode(6)
        l22 = ListNode(4)
        l2.next, l21.next = l21, l22

        ret = self.s.addTwoNumbers(l1, l2)
        rnode = ListNode(7)
        r1 = ListNode(0)
        r2 = ListNode(8)
        rnode.next, r1.next = r1, r2
        self.assertEqual(ret, rnode)


if __name__ == '__main__':
    unittest.main()

