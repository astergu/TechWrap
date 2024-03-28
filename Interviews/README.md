- [数据结构](#数据结构)
  - [Stack](#stack)
    - [Linked-list Implementation](#linked-list-implementation)
    - [Resizing Array Implementation](#resizing-array-implementation)
  - [Queue](#queue)
    - [Linked-list Implementation](#linked-list-implementation-1)
    - [Resizing Array Implementation](#resizing-array-implementation-1)
  - [Dictionaries](#dictionaries)
  - [Binary Search Trees 二叉搜索树](#binary-search-trees-二叉搜索树)
  - [Heap](#heap)
- [算法](#算法)
  - [Sorting 排序](#sorting-排序)
    - [Permutation Sort 组合排序](#permutation-sort-组合排序)
    - [Bubble Sort 冒泡排序](#bubble-sort-冒泡排序)
    - [Selection Sort 选择排序](#selection-sort-选择排序)
    - [Insertion Sort 插入排序](#insertion-sort-插入排序)
    - [Merge Sort 归并排序 \*](#merge-sort-归并排序-)
    - [Quick Sort 快速排序 \*](#quick-sort-快速排序-)
    - [Bucket Sort 桶排序 \*](#bucket-sort-桶排序-)
    - [Topological Sort 拓扑排序](#topological-sort-拓扑排序)
  - [Searching 搜索算法](#searching-搜索算法)
    - [Binary Search 二分搜索](#binary-search-二分搜索)
  - [Union-Find 并查集](#union-find-并查集)
    - [Quick-Find](#quick-find)
    - [Quick-Union](#quick-union)
      - [Lazy approach](#lazy-approach)
      - [Weighted quick-union](#weighted-quick-union)
      - [Weighted Quick union with path compression](#weighted-quick-union-with-path-compression)
  - [Depth-First Search 深度优先搜索](#depth-first-search-深度优先搜索)
  - [Sliding Window 滑动窗口](#sliding-window-滑动窗口)
  - [Divide-and-Conquer 分治算法](#divide-and-conquer-分治算法)
- [Interview Questions 面试题](#interview-questions-面试题)
  - [Cracking the Code Interview 面试题](#cracking-the-code-interview-面试题)
    - [Sorting and Searching 排序和搜索](#sorting-and-searching-排序和搜索)

<br>

| 数据结构 | 适合问题 | 解决思路 |
| -------- | -------- | ------- |
| Stack | | |
| Queue | | |
| Tree | | |

<br>

| 算法 | 适合问题 | 解决思路 | 时间复杂度 |
| ------- | ------- | ------- | ------ |
| Union-Find 并查集 | 动态连通性，e.g. `判定合法等式` | - 把原始问题抽象为图论问题 <br> - 很多使用DFS解决的问题，也可以用Union-Find算法解决 | - 基本实现：O(N) <br> - 平衡性优化+路径压缩：O(logN) |
| Depth-First Search 深度优先搜索 | | | |
| Breadth-First Search 广度优先搜索 | | | |
| Sliding Window 滑动窗口 | 最长** | | |


<br>

# 数据结构

本质上，两种数据结构：`array-based`和`pointer-based`。

- **Arrays**（数组）
  - 连续分配 contiguously-allocated
  - 随机访问
  - 优点
    - 常数时间访问 constant-time access given the index
    - 空间效率 space efficiency
    - 存储 memory locality
  - 缺点
    - 不能随时修改size
- **Lists** (链表)
  - 优点
  - 缺点
  - 操作
    - Search
    - Insert
    - Delete


## Stack

Last-in, first-out (LIFO)

- *Push(x, s)*: Insert item *x* at the top of stack *s*.
- *Pop(s)*: Return (and remove) the top item of stack *s*.

### Linked-list Implementation

- Every operation takes constant time in the work case.
- Use extra time and space to deal with links.

### Resizing Array Implementation

- Every operation takes constant amortized time.
- Less wasted space.

## Queue

First-in, First-out (FIFO)

- *Enqueue(x, q)*: Insert item *x* at the back of the queue *q*.
- *Dequeue(q)*: Return (and remove) the front item from queue *q*.

### Linked-list Implementation

### Resizing Array Implementation

## Dictionaries

The primary operations of dictionary support are:

- *Search(D, k)*: Given a search key *k*, return a pointer to the element in dictionary *D* whose key value is *k*, if one exists.
- *Insert(D, x)*: Given a data item *x*, add it to the set in the dictionary *D*.
- *Delete(D, x)*: Given a pointer to a given data item *x* in the dictionary *D*, remove it from *D*.

| Dictionary operation | Unsorted array | Sorted array | 
| ----------- | ------- | ------- |
| Search(L, k) | $O(n)$ | $O(logn)$ |
| Insert(L, x) | $O(1)$ | $O(n)$ |
| Delete(L, x) | $O(1)^*$ | $O(n)$ |
| Successor(L, x) | $O(n)$ | $O(1)$ |
| Predecessor(L, x) | $O(n)$ | $O(1)$ |
| Minimum(L, x) | $O(n)$ | $O(1)$ |
| Maximum(L, x) | $O(n)$ | $O(1)$ |


## Binary Search Trees 二叉搜索树



## Heap

# 算法

## Sorting 排序

| Sorting | Time | Space | 
| ----- | ----- | ----- | 
| Bubble Sort | $O(n^2)$ average/worst | $O(1)$ |
| Selection Sort | $O(n^2)$ average/worst | $O(1)$ |
| Merge Sort | $O(nlogn)$ average/worst | |
| Quick Sort | $O(nlogn)$ average, $O(n^2)$ worst | $O(logn)$ |
| Radix Sort | $O(kn)$ | |


### Permutation Sort 组合排序

```python
def permutation_sort(A):
    for B in permutations(A):
        if is_sorted(B):
            return B
```

- enumerate permutations: $\Omega(n!)$
- check if permutation is sorted: $O(n)$ 
- overall runtime: $\Omega(n!n)$

### Bubble Sort 冒泡排序

```python
def bubble_sort(A):
    n = len(A)
    for i in range(1, n - 1):
        for j in range(n, -1, i + 1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
```

### Selection Sort 选择排序 

```python
def selection_sort(A):
    for i in range(len(A) - 1, 0, -1): # O(n) loop over array
        m = i                          # O(1) initial index of max
        for j in range(i):             # O(i) search for max in A[:i]
            if A[m] < A[j]:            # O(1) check for large value
                m = j                  # O(1) new max found
        A[m], A[i] = A[i], A[m]        # O(1) swap
```

- overall runtime: $\Theta(n^2)$

### Insertion Sort 插入排序 

1. 从未排序序列中抽出下一个待排序项*A[i]*；
2. 将这个待排序项与已排序序列中的项依次做比较，直到插入合适的位置；

```python
def insertion_sort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            A[j-1], A[j] = A[j], A[j-1] # swap
            j = j - 1
```

- overall runtime: $\Theta(n^2)$

### Merge Sort 归并排序 *

```python
def merge_sort(A, p, r):
    if p >= r:
        return
    q = (p + r) // 2
    merge_sort(A, p, q)
    merge_sort(A, q + 1, r)
    merge(A, p, q, r)

def merge(A, p, q, r):
    pl = q - p + 1
    pr = r - q

```

- overall runtime: $\Theta(nlogn)$

### Quick Sort 快速排序 *

### Bucket Sort 桶排序 *

### Topological Sort 拓扑排序

## Searching 搜索算法

### Binary Search 二分搜索

```python
def binary_search(A, x): # A: sorted array, x: key 
    low, high = 0, len(A) - 1
    while low <= high:
        mid = low + ((high-low) >> 1)
        if A[mid] < x:
            low = mid + 1
        elif A[mid] > x:
            high = mid - 1
        else:
            return mid
```

## Union-Find 并查集

| 算法 | 初始化 | union | find | 缺点 |
| ------ | ------- | ------ | ------- | ------- |
| quick-find | N | N | 1 | 1. Union too expensive (N array accesses). <br> 2. Trees are flat, but too expensive to keep them flat.
| quick-union | N | N | N | 1. Trees can get tall. <br> 2. Find too expensive (could be N array accesses).|
| weighted QU | N | lgN | lgN | |

<br>

> **M union-find operations on a set of N objects**

| 算法 | worst-case time | 
| ------- | -------- |
| quick-find | M N |
| quick-union | M N |
| weighted QU | N + M logN |
| QU + path compression | N + MlogN |
| weighted QU + path compression | N + Mlg*N |

> lg*N: The number of times you have to take the log of N to get 1.


### Quick-Find

代码框架： 

```python
class QuickFind(object):
    def __init__(self, N): # set id of each object to itself
        self.id = [i for i in range(N)]

    def connected(p, q): # check whether p and q are in the same component
        return self.id[p] == self.id[q]
    
    def union(p, q): # check all entries with id[p] to id[q] (at most 2N+2 array accesses)
        pid, qid = id[p], id[q]
        for i in range(len(id)):
            if id[i] == pid:
                id[i] = qid
```

> 初始化：O(N)，Union：O(N)，Find：O(N)

### Quick-Union

#### Lazy approach

```python
class QuickUnion(object):
    def __init__(self, N): # set id of each object to itself
        self.id = [i for i in range(N)]

    def root(i): # chase parent pointers until reach root
        while i != id[i]:
            i = id[i]
        return i

    def connected(p, q): # check if p and q have same root
        return root(p) == root(q)

    def union(p, q): # change root of p to point to root of q
        i, j = root(p), root(q)
        id[i] = j 
```

#### Weighted quick-union

1. Modify quick-union to avoid tall trees.
2. Keep track of size of each tree (number of objects).
3. Balance by linking root of smaller tree to root of larger tree.

```python
class WeightedQuickUnion(object):
    def __init__(self, N): # set id of each object to itself
        self.id = [i for i in range(N)]
        self.size = [1] * N

    def root(i): # chase parent pointers until reach root
        while i != id[i]:
            i = id[i]
        return i

    def connected(p, q): # check if p and q have same root
        return root(p) == root(q)

    def union(p, q): # link root of smaller tree to root of larger tree
        i, j = root(p), root(q)
        if i == j:
            return
        if (self.size[i] < self.size[j]):
            id[i] = j
            self.size[j] += self.size[i]
        else:
            id[j] = i
            self.size[i] += self.size[j]
```

#### Weighted Quick union with path compression

Just after computing the root of p, set the id of each examined node to point to that root.

```python
class WeightedQuickUnionWithPathCompression(object):
    def __init__(self, N): # set id of each object to itself
        self.id = [i for i in range(N)]
        self.size = [1] * N

    def root(i): # chase parent pointers until reach root
        while i != id[i]:
            id[i] = id[id[i]]
            i = id[i]
        return i

    def connected(p, q): # check if p and q have same root
        return root(p) == root(q)

    def union(p, q): # link root of smaller tree to root of larger tree
        i, j = root(p), root(q)
        if i == j:
            return
        if (self.size[i] < self.size[j]):
            id[i] = j
            self.size[j] += self.size[i]
        else:
            id[j] = i
            self.size[i] += self.size[j]
```

> In theory, WQUPC is not quite linear. <br>
> In practice, WQUPC is linear. <br>
> No linear-time algorithm exists.

## Depth-First Search 深度优先搜索

代码框架：

```python
```


## Sliding Window 滑动窗口

代码框架：

```python
def sliding_window(nums):
    # Iterate over elements in our input
        # Expand the window
        # Meet the condition to stop expansion
            # Process the current window
            # Contract the window
```

## Divide-and-Conquer 分治算法

- **Divide** the problem into one or more subproblems that are smaller instances of the same problem.
- **Conquer** the subproblems by solving them recursively.
- **Combine** the subproblem solutions to form a solution to the original problem.


# Interview Questions 面试题

## Cracking the Code Interview 面试题

### Sorting and Searching 排序和搜索

1. **Sorted Merge** [`leetcode 88`](https://leetcode.com/problems/merge-sorted-array/description/): You are given two sorted arrays A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.

```python
def sort_merge(A, B):
    m, n = len(A), len(B)
    k = m + n - 1 # last index of the final array
    i, j = m - 1, n - 1
    while i >= 0 and j >= 0:
        if A[i] > B[j]: 
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        A[k] = B[j]
        j -= 1
        k -= 1
```

> Time: $O(m+n)$

2. **Group Anagrams** [`leetcode 49`](https://leetcode.com/problems/group-anagrams/description/): Write a method to sort an array of strings so that all the anagrams are next to each other.

```python
def group_anagrams():
    from collections import defaultdict
        dct = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            if key in dct:
                dct[key].append(s)
            else:
                dct[key] = [s]
        return dct.values()
```

> Time: $O(nmlogm)$

3. **Search in Rotated Array** [`leetcode 33`](https://leetcode.com/problems/search-in-rotated-sorted-array/description/): Given a sorted array of *n* integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order.

```python
def search_in_rotated_sorted_array(nums, target):
    low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]: # reversed 
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
```

> Time: $O(logn)$ <br>
> - `Follow up`
>   - may have duplicate items [leetcode 81: Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/)

4. **Sorted Search, No Size**: You are given an array-like data structure `Listy` which lacks a size method. It does, however, have an `elementAt(i)` method that returns the element at index i in O(1) time. If i is beyond the bounds of the data strucutre, it return -1. (For this reason, the data structure only supports positive integers.) Given a `Listy` which contains sorted, positive integers, find the index at which an element x occurs. If x occurs multiple times, you may return any index.
5. **Sparse Search**: Given an sorted array of strings that is interspersed with empty strings, write a method to find the location of a given string.
6. **Sort Big File**: Imagine you have a 20GB file with one string per line. Explain how you would sort the file.
7. **Missing Int**: Given an input file with four billion non-negative integers, provide an algorithm to generate an integer that is not contained in the file. Assume you have 1GB of memeory available for this task.

- Follow up
  - What if you have only 10MB of memory? Assume that all the values are distinct and we now have no more than one billion non-negative integers.

8. **Find Duplicates**: You have an array with all the numbers from 1 to N, where N is at most 32,000. The array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory available, how would you print all duplicate elements in the array?
9. **Sorted Matrix Search**: Given an $M\times N$ matrix in which each row and each column is sorted in ascending order, write a method to find an element.
10. **Rank from Stream**: Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal to x). Implement the data structures and algorithms to support these operations. That is, implement the method `track(int x)`, which is called when each number is generated, and the method `getRankOfNumber(int x)`, which returns the number of values less than or equal to x (not including x itself).
11. **Peaks and Valleys**: In an array of integers, a "peak" is an element which is greater than or equal to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an array of integers, sort the array into an alternating sequence of peaks and valleys.  