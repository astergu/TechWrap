# Practical Tips

- Array problems often have simple brute-force solutions that use *O(n)* space, but there are subtler solutions that **use the array itself** to **reduce space** complexity to *O(1)*.
- Filling an array from the front is slow, so see if it's possible to **write values from the back**.
- Instead of deleting an entry (which requires moving all entries to its right), consider **overwriting** it.
- When dealing with integers encoded by an array consider **processing the digits from the back** of the array. Alternatively, reverse the array so the **least-significant digit is the first entry**.
- **Dutch National Flag Problem** (quicksort)
```python
def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
```
Each iteration decreases the size of *unclassified* by 1, and the time spent within each iteration is *O(1)*, implying the time complexity is *O(n)*. The space complexity is clearly *O(1)*.
    - **Variant**: Assuming that keys take on of three values, reorder the array so that all objects with the same key appear together. The order of the subarray is not important.
    - **Variant**: Given an array *A* of *n* objects with keys that takes one of four values, reorder the array so that all objects that have the same key appear together. Use *O(1)* additional space and *O(n)* time.
    - **Variant**: Given an array *A* of *n* objects with Boolean-valued keys, reorder the array so that objects that have the key false appear first. Use *O(1)* additional space and *O(n)* time.
    - *Variant*: Given an array *A* of *n* objects with Boolean-valued keys, reorder the array so that objects that have the key false appear first. The relative ordering of objects with key true should not change. Use *O(1)* additional space and *O(n)* time.
- **PrefixSum Array**

prefixSum[x] = sum of subarray(0, x) 
             = nums[0] + nums[1] + ... + nums[x] 

# Algorithm Questions about Arrays

reference: [tech-interview-handbook/array](https://github.com/yangshun/tech-interview-handbook/blob/master/algorithms/array.md)

- [Subarray Sum Equals K](SubarraySumEqualsK.py)
    - 利用prefixSum，只遍历一次便可得到全部的subarray sum，另外利用额外的map来记录之前的结果，最终时间复杂度为O(N)，空间复杂度为O(N)。
- [Subarray with given sum](SubarrayWithGivenSum.py)
    - link: [https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0](https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0)
- [Minimum Size Subarray Sum](MinimumSizeSubarraySum.py) 
- In an array of arrays, e.g. given `[[], [1, 2, 3], [4, 5], [], [], [6, 7], [8], [9, 10], [], []]`, print `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`
    - Implement an iterator that supports `hasNext()`, `next()`, and `remove()` methods.
- Given a list of item prices, find all possible combinations of items that sum a particular value `K`.
- Paginate an array with constraints, such as skipping certain items.
- Implement a circular buffer using an array.
- Given an array of arrays, sort them in ascending order.
- Given an array of integers, print out a histogram using the said array; include a base layer (all stars).
    - E.g. `[5, 4, 0, 3, 4, 1]`
```
*
**  *
** **
** **
** ***
******
```
- Given an array and an index, find the product of the elements of the array except the element at that index.
- Given a set of rectangles represented by a height and an interval along the y-axis, determine the size of its union.
- Given 2 separate arrays, write a method to find the values that exist in both arrays and return them.
- Given an array of integers find whether there is a sub-sequence that sums to 0 and return it.
  - E.g. `[1, 2, -3, 1]` => `[1, 2, -3]` or `[2, -3, 1]`.
- Given an input array and another array that describes a new index for each element, mutate the input array so that each element ends up in their new index. Discuss the runtime of the algorithm and how you can be sure there would not be any infinite loops.
- Given an array of non-negative numbers, find continuous subarray with sum to S.
  - [Source](http://blog.gainlo.co/index.php/2016/06/01/subarray-with-given-sum/).
- Given an array of numbers list out all triplets that sum to 0. Do so with a running time of less than O(n^3).
  - [Source](http://blog.gainlo.co/index.php/2016/07/19/3sum/).
- Given an array of numbers list out all quadruplets that sum to 0. Do so with a running time of less than O(n^4).
- Given an array of integers, move all the zeroes to the end while preserving the order of the other elements. You have to do it in-place and are not allowed to use any extra storage.
- Given an array of integers, find the subarray with the largest sum. Can you do it in linear time.
  - Maximum subarray sum problem.
- You have an array with the heights of an island (at point 1, point 2 etc) and you want to know how much water would remain on this island (without flowing away).
  - Trapping rain water question.
- Given an array containing only digits `0-9`, add one to the number and return the array.
  - E.g. Given `[1, 4, 2, 1]` which represents `1421`, return `[1, 4, 2, 2]` which represents `1422`.
- Find the second maximum value in an array.
- Given an array, find the longest arithmetic progression.
- Rotate an array by an offset of k.
- Remove duplicates in an unsorted array where the duplicates are at a distance of k or less from each other.
- Given an unsorted list of integers, return true if the list contains any duplicates within k indices of each element. Do it faster than O(n^2).
- Given an unsorted list of integers, return true if the list contains any fuzzy duplicates within k indices of each element. A fuzzy duplicate is another integer within d of the original integer. Do it faster than O(n^2).
  - E.g. If d = 4, then 6 is a fuzzy duplicate of 3 but 8 is not.
- Say you have an unordered list of numbers ranging from 1 to n, and one of the numbers is removed, how do you find that number? What if two numbers are removed?
- Given an array of string, find the duplicated elements.
  - [Source](http://blog.gainlo.co/index.php/2016/05/10/duplicate-elements-of-an-array/).
- Given an array of integers, find a maximum sum of non-adjacent elements.
  - E.g. `[1, 0, 3, 9, 2]` should return `10 (1 + 9)`.
  - [Source](http://blog.gainlo.co/index.php/2016/12/02/uber-interview-question-maximum-sum-non-adjacent-elements/)
- Given an array of integers, modify the array by moving all the zeros to the end (right side). The order of other elements doesn't matter.
  - E.g. `[1, 2, 0, 3, 0, 1, 2]`, the program can output `[1, 2, 3, 1, 2, 0, 0]`.
  - [Source](http://blog.gainlo.co/index.php/2016/11/18/uber-interview-question-move-zeroes/).
- Given an array, return the length of the longest increasing contiguous subarray.
  - E.g., `[1, 3, 2, 3, 4, 8, 7, 9]`, should return `4` because the longest increasing array is `[2, 3, 4, 8]`.
  - [Source](http://blog.gainlo.co/index.php/2017/02/02/uber-interview-questions-longest-increasing-subarray/).
- Given an array of integers where every value appears twice except one, find the single, non-repeating value. Follow up: do so with O(1) space.
  - E.g., `[2, 5, 3, 2, 1, 3, 4, 5, 1]` returns 4, because it is the only value that appears in the array only once.


## Other Sources
- [] *K*th smallest element in an array 
- [x] [Rotate and Delete](RotateAndDelete.py): Given an array of numbers (e.g. integers), there are two kinds of operations: rotate (clock-wise) and delete. 
Rotate the array *n* times and then delete the *n*th last element. If the *n*th last element does not exist then
deletes the first element present in the array. Your task is to find out which is the last
element that you deletes from the array so that the array becomes empty after removing it.
    - source: [https://practice.geeksforgeeks.org/problems/rotate-and-delete/0] (https://practice.geeksforgeeks.org/problems/rotate-and-delete/0)
