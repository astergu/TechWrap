'''
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false
'''

from typing import Optional
from ListNode import ListNode, ListNodeGenerator

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        n = len(vals)
        for i in range(n >> 1):
            if vals[i] != vals[n - 1 - i]:
                return False
        
        return True


if __name__ == '__main__':
    sol = Solution()
    vals = [1,2]
    head = ListNodeGenerator(vals).head
    print(sol.isPalindrome(head))