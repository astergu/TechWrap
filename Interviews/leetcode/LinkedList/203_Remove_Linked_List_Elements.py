'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''

from ListNode import ListNode, ListNodeGenerator
from typing import Optional

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next


if __name__ == '__main__':
    sol = Solution()
    vals = [7,7,7,7]
    val = 7 
    head = ListNodeGenerator(vals).head
    ret = sol.removeElements(head, val)
    while ret:
        print(ret.val)
        ret = ret.next