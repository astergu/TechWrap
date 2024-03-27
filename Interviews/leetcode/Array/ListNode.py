# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListGenerator:
    def __init__(self, vals):
        if not vals:
            raise Exception("ListGenerator can't initialize with empty values!")
        dummy = ListNode(-1)
        prev = dummy
        for v in vals:
            n = ListNode(v)
            prev.next = n
            prev = prev.next
        
        self.start = dummy.next