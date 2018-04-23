## Practical Tips

A *heap* is a specialized binary tree. The keys must satisfy the *heap property*---the key at each node is at least as great as the keys stored at its children. A max-heap can be implemented as an array; the children of the node at index *i* are at indices *2i+1* and *2i+2*.

A max-heap supports *O(logn)* insetions, *O(1)* time lookup for the max element, and *O(logn)* deletion of the max element.

- Use a heap when **all you care about** is the **largest** or **smallest** elements, and you **do not need** to support fast lookup, delete, or search operations for arbitrary elements.
- A heap is a good choice when you need to compute the *k* **largest** or *k* **smallest** elements in a collection. For the former, use a min-heap, for the latter, use a max-heap.


## Base problems

- Suppose you were asked to write a program which takes a sequence of strings presented in "streaming" fashion: you cannot back up to read an earlier value. Your program must compute the *k* longest strings in the sequence. All that is required is the *k* longest strings---it is not required to order these strings.
```python
def top_k(k, stream):
    # Entries are compared by their lengths
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)
    for next_string in steam:
        # Push next_string and pop the shortest string in min_heap.
        heapq.heappushpop(min_heap, (len(next_string), next_string))
   return [p[1] for p in heapq.nsmallest(k, min_heap)] 
```
Each string is processed in *O(logk)* time, which is the time to add and to remove the minimum element from the heap.
- **Merge Sorted Files**
    - **Description**: You are given 500 files, each containing stock trade information for an S&P 500 company. Each trade is encoded by a line in the following format: 123211, AAPL, 30, 456.12. The first number is the time of the trade expressed as the number of milliseconds since the start of the day's trading. Lines within each file are sorted in increasing order of time. The remaining values are the stock symbol, number of shares, and price. You are to create a single file containing all the trades from the 500 files, sorted in the order of increasing trade times. The individual files are of the order of 5-100 megabytes; the combined file will be of the order of five gigabytes.
    - *Write a program that takes as input a set of sorted sequences and computes the union of these sequences as a sorted sequence.* For example, if the input is <3, 5, 7>, <0, 6>, and <0, 6, 28>, then the output is <0, 0, 3, 5, 6, 6, 7, 28>.
```python
def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]
    # Puts first element from each iterator in min_heap.
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result

# Pythonic solution, uses the heapq.merge() method which takes multiple inputs.
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))
```
