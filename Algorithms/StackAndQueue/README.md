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
Time complexity *O(1)*, space complexity *O(n)*.


- A *queue* supports two basic operations---enqueue and dequeue. A queue can be implemented
using a linked list, in which case these operations have *O(1)* time complexity.
- [x] Given a binary tree, return an array consisting of the keys at the same level. Keys
should appear in the order of the corresponding nodes' depths, breaking ties from left to
right.  
```python
def binary_tree_depth_order(tree):
    result, curr_depth_nodes = [], collections.deque([tree])
    while curr_depth_nodes:
        next_depth_nodes, this_level = collections.deque([]), []
        while curr_depth_nodes:
            curr = curr_depth_nodes.popleft()
            if curr:
                this_level.append(curr.data)
                next_depth_nodes += [curr.left, curr.right]

        if this_level:
            result.append(this_level)
        curr_depth_nodes = next_depth_nodes
    return result
``` 
Time complexity is *O(n)*, space complexity is *O(m)*, where *m* is the maximum number of nodes
at any single depth.
    - **Variant**: Write a program which takes as input a binary tree and returns the keys in top down, alternating left-to-right and right-to-left order, starting from left-to-right.
    - **Variant**: Write a program which takes as input a binary tree and returns the keys in a bottom up, left-to-right order.
    - **Variant**: Write a program which takes as input a binary tree with integer keys, and returns the average of the keys at each level.



## Questions
- 
- [x] [Longest Valid Parentheses](LongestValidParentheses.py)
    - link: [https://leetcode.com/problems/longest-valid-parentheses/description/](https://leetcode.com/problems/longest-valid-parentheses/description/)
