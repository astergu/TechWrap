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

Dynamic Programming (动态规划)

### Naive Solution (Space: O(N^2), Time: O(1))

### Sqrt Solution (Space: O(N), Time: O(sqrt(N))

### Sparse Table (ST) Algorithm Solution

A better approach is to preprocess RMQ for sub arrays of length `2^k` using dynamic programming. We will keep an array M\[0, N-1\]\[0, logN\] where M[i][j] is the index
of the minimum value in the sub array starting at `i` having length `2^j`. For example:

![Sparse Table example](https://community.topcoder.com/i/education/lca/RMQ_003.gif)

For computing `M[i][j]` we must search for the minimum value in the first and second 
half of the interval. It's obvious that the small pieces have `2^(j-1)` length, so
the recurrence is:
![Sparse Table formula](https://community.topcoder.com/i/education/lca/RMQ_007.gif)

Once we have these values preprocessed, RMQ(i, j) can be calculated through:
![RMQ formula](https://community.topcoder.com/i/education/lca/RMQ_005.gif)

So the time complexity is O(1), space complexity is O(NlogN).

### Segment Trees (线段树)


## Use Cases:

### Lowest Common Ancestor Problem (LCA) 最低共同祖先问题


### Longest Common Prefix Problem (LCP)

## Reading Materials

[https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor/](https://www.topcoder.com/community/data-science/data-science-tutorials/range-minimum-query-and-lowest-common-ancestor/)
