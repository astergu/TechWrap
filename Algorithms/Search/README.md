## Practical Tips

### Binary Search 二分查找
```python
def bsearch(t, A):
    L, U = 0, len(A) - 1
    while L <= U:
        M = L + (U - L) / 2  # instead of (L + U) // 2
        if A[M] < t:
            L = M + 1
        elif A[M] == t:
            return M
        else:
            U = M - 1
    return -1
```
Time complexity *O(logn)*.



### python bisect
- link: [https://docs.python.org/2/library/bisect.html](https://docs.python.org/2/library/bisect.html)
