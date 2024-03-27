'''
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:

Build the result list and return its head.
'''

from leetcode.Array.ListNode import ListNode, ListGenerator

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i = 0
        ans = list1
        start, end = None, None
        while i < b:
            i += 1
            if i == a:
                start = list1 
            if i == b:
                end = list1.next.next
            list1 = list1.next

        start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end

        return ans 


if __name__ == '__main__':
    sol = Solution()
    list1 = ListGenerator([10,1,13,6,9,5]).start
    a = 3
    b = 4
    list2 = ListGenerator([1000000,1000001,1000002]).start
    ret = sol.mergeInBetween(list1, a, b, list2)
    while ret:
        print(ret.val)
        ret = ret.next