## Practical Tips

- The last-in, first-out semantics of a stack make it very useful for creating reverse iterators for sequences which are stored in a way that would make it difficult or impossible to step back from a given element.
```python
def print_linked_list_in_reverse(head):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    while nodes:
        print ndoes.pop()
```
The time and space complexity are *O(n)*, where *n* is the number of nodes in the list.
- Consider **augmenting** the basic stack or queue data structure to support additional
operations, such as finding the maximum element.
- **Design a stack that includes a max operation, in addition to push and pop.**
```python
class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max())))
```


## Questions

- [x] [Longest Valid Parentheses](LongestValidParentheses.py)
    - link: [https://leetcode.com/problems/longest-valid-parentheses/description/](https://leetcode.com/problems/longest-valid-parentheses/description/)
