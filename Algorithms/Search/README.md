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

- Example: **GPA searching**
```python
Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

def comp_gpa(student):
    return (-student.grade_point_average, student.name)

def search_student(stduetns, target, comp_gpa):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target
```

- **searching libraries**
    - The *bisect* module provides binary search functions for sorted list. Specifically, assuming *a* is a sorted list.
    - To find the first element that is not less than a targeted value, use *bisect.bisect_left(a, x)*.
    - To find the first element that is greater than a targeted value, use *bisect.bisect_right(a, x)*.
- **Write a method that takes a sorted array and a key and returns the index of the *first* occurrence of that key in the array**.
```python
def search_first_of_k(A, k):
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
```
Time complexity is *O(logn)*.
- **Variant**: Design an efficient algorithm that takes a sorted array and a key, and finds the index of the *first* occurrence of an element greater than the key.
- **Variant**: Let A be an unsorted array of *n* integers, with A[0] >= A[1] and A[n-2] <= A[n-1]. Call an index *i* a *local minimum* if *A[i]* is less than or equal to its neighbors. How would you efficiently find a local minimum, if one exists?
- **Variant**: Write a program which takes a sorted array *A* of integers, and an integer *k*, and returns the interval enclosing *k*, i.e., the pair of integers *L* and *U* such that *L* is the first occurrence of *k* in *A* and *U* is the last occurrence of *k* in *A*. If *k* does not appear in *A*, return [-1, -1]. For example if A=<1, 2, 2, 4, 4, 4, 7, 11, 11, 13> and *k*=11, you should return [7, 8].
- **Variant**: Write a program which tests if *p* is a prefix of a string in an array of sorted strings.


### python bisect
- link: [https://docs.python.org/2/library/bisect.html](https://docs.python.org/2/library/bisect.html)
