class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNodeGenerator:
    def __init__(self, vals):
        self.head = ListNode(-1)
        prev = self.head
        for v in vals:
            prev.next = ListNode(v)
            prev = prev.next
        
        self.head = self.head.next
