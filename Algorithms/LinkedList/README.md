## Practical Tips

**Definition:**
```python
class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
```

**Search for a key:**
```python
def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L
```

**Insert a new node after node:**
```python
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node
```

**Delete a node:**
```python
def delete_after(node):
    node.next = node.next.next
```

- List problems often have a simple brute-force solution that uses *O(n)* space,
but a subtler solution that uses the **existing list nodes** to reduce space complexity to *O(1)*.
- Very often, a problem on lists is conceptually simple, and is more about **cleanly coding what's 
specified**, rather than designing an algorithm.
- Consider using a **dummy head** (sometimes referred to as a sentinel) to avoid having to check for empty
lists. This simplifies code, and makes bugs less likely.
- It's easy to forget to **update next** (and previous for double linked list) for the head
and tail.
- Algorithms operating on singly linked lists often benefit from using **two iterators**, one
ahead of the other, or one advancing quicker than the other.

## Common Questions
- **Test for Cyclicity**
```python
def has_cycle(head):
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
    return None
```
