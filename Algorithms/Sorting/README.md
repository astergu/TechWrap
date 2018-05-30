Naive sorting algorithms run in *O(n<sup>2</sup>)* time. A number of sorting algorithms run in *O(nlogn)* time---heapsort, merge sort, and quicksort are examples. Each has its advantages and disadvantages: for example, *heapsort* is in-place but not stable; merge sort is stable but not in-place; quicksort runs *O(n<sup>2</sup>)* time in worst-case. (An in-place sort is one which uses *O(1)* space; a stable sort is one where entries which are equal appear in their original order.)

For short arrays, e.g., 10 or fewer elements, insertion sort is easier to code and faster than asymptotically superior sorting algorithms. If every element is known to be at most *k* places from its final location, a min-heap can be used to get an *O(nlogk)* algorithm.


- For **specialized input**, e.g., a very small range of values, or a small number of values, it's possible to sort in *O(n)* time rather than *O(nlogn)* time.

## Basic Practice

**Selection Sort**
```cpp
void selectionSort(int arr[], int n)
{
    int i, j, min_idx;
 
    // One by one move boundary of unsorted subarray
    for (i = 0; i < n - 1; i++)
    {
        // Find the minimum element in unsorted array
        min_idx = i;
        for (j = i + 1; j < n; j++)
          if (arr[j] < arr[min_idx])
            min_idx = j;
 
        // Swap the found minimum element with the first element
        swap(&arr[min_idx], &arr[i]);
    }
}
```

### Compute the Intersection of Two Sorted Arrays

**Write a program which takes as input two sorted arrays, and returns a new array containing elements that are present in both of the input arrays. The input arrays may have duplicate entries, but the returned array should be free of duplicates.** For example, the input is <2, 3, 3, 5, 5, 6, 7, 7, 8, 12> and <5, 5, 6, 8, 8, 9, 10, 10>, your output should be <<5, 6, 8>.

- Solution 1: the brute-force algorithm has *O(mn)* time complexity.
- Solution 2: iterate throught the first array and use binary search.
```python
def intersect_two_sorted_arrays(A, B):
    def is_present(k):
        i = bisect.bisect_left(B, k)
        return i < len(B) and B[i] == k

    return [a for i, a in enumerate(A) if (i == 0 or a != A[i - 1]) and is_present(a)]
```
The time complexity is *O(mlogn)*, where *m* is the length of the array being iterated over.
- Solution 3: exploit the fact that both arrays are sorted.
```python
def intersect_two_sorted_arrays(A, B):
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intsection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else:   # A[i] > B[j].
            j += 1
    return intersection_A_B
```
Since we spend *O(1)* time per input array element, the time complexity for the entire algorithm is *O(m + n)*.


### Render A Calendar

**Write a program that takes a set of events, and determines the maximum number of events that take place concurrently.**

