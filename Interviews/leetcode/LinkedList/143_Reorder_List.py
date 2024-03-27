'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''
from typing import Optional
from ListNode import ListNode, ListNodeGenerator

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        deque = []
        while curr:
            deque.append(curr)
            curr = curr.next

        if len(deque) == 1:
            return

        prev = None
        while len(deque) >= 2:
            front, back = deque.pop(0), deque.pop()
            front.next = back
            if prev:
                prev.next = front
            prev = back
        
        if deque:
            prev.next = deque.pop()
            prev.next.next = None
        else:
            prev.next = None

    def reorderList2(self, head: Optional[ListNode]) -> None:
        res = ListNode(0)
        res.next = head
        slow = fast = res
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        fast = self.reverseTwo(fast)
        slow = res.next
        while fast:
            slowp, fastp = slow.next, fast.next
            slow.next, fast.next = fast, slowp
            slow, fast = slowp, fastp
        return res.next

    def reverseTwo(self, node):
        prev = None
        curr = node
        while curr:
            nextp = curr.next
            curr.next = prev
            prev = curr
            curr = nextp
        return prev


if __name__ == '__main__':
    sol = Solution()
    vals = [1, 2, 3, 4]
    head = ListNodeGenerator(vals).head
    sol.reorderList(head)
    while head:
        print(head.val)
        head = head.next