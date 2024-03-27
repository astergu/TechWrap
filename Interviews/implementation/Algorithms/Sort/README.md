- [Selection Sort](#selection-sort)
- [Insertion Sort](#insertion-sort)
- [Shell Sort](#shell-sort)


# Selection Sort

> - Select Sort uses $N^2/2$ compares and $N$ exchanges.
> - Running time insensitive to input. Quadratic time, even if input is sorted.
> - Data movement is minimal. Linear number of exchanges.

```python
"""
- Entries to the left of the pointer are in ascending order.
- No entry to the right of the pointer is smaller than any entry to the left of the pointer. 
"""
def selection_sort(items):
    for i in range(len(items)):
        curr_min = i
        for j in range(i + 1, len(items)):
            if items[j] < items[curr_min]:
                items[j], items[curr_min] = items[curr_min], items[j]
```

# Insertion Sort

> - To sort a randomly-ordered array with distinct keys, insertion sort use $~1/4N^2$ compares and $~1/4N^2$ exchanges on average.
> - *Best case*: If the array is in ascending order, insert sort makes $N-1$ compares and 0 exchanges.
> - *Worst case*: If the array is in descending order (and no duplicates), insertion sort makes $~1/2N^2$ compares and $~1/2N^2$ exchanges.
> - For partially-sorted arrays, insertion sort runs in linear time.
 
```python
"""
- Entries to the left of the pointer are in ascending order.
- Entries to the right of the pointer have not yet been seen.
"""
def insertion_sort(items):
    for i in range(len(items)):
        for j in range(i, 0, -1):
            if items[j] < items[j - 1]:
                items[j], items[j - 1] = items[j - 1], items[j]
```

# Shell Sort

> *Idea*: Move entries more than one position at a time by `h-sorting` the array.