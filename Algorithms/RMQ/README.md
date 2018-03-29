# Range Minimum Query 区间最值查询

According to Wikipedia, Range Minimum Query (RMQ) solves the problem
of finding the minimal value in a sub-array of an array of comparable
objects.

ST(Sparse Table)算法是一个非常有名的在线处理RMQ问题的算法，它可以在O(NlogN)时间内
进行预处理，然后在O(1)时间内回答每个查询。
这问题可以用线段树来解决，算法复杂度为O(N)~O(logN).


## Definition
[https://en.wikipedia.org/wiki/Range_minimum_query](https://en.wikipedia.org/wiki/Range_minimum_query)

## Solution

### Naive Solution

The array is static, which means it won't change, but the queries are online.
So we can precompute the minimum value of any (i, j). The precomputed results
can take O(n^2) space, using dynamic programming.

```cpp
result[i][j] = min(array[i:j + 1])
```



###

## Use Cases:

- Lowest Common Ancestor Problem (LCA)
- Longest Common Prefix Problem (LCP)

## Reading Materials

[https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor/](https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor/)