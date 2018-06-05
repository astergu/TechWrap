## Basic Knowledge

### DFS vs. BFS

DFS和BFS的时间复杂度都是O(V+E)

## References


## Questions
- [Number of Islands](NumberOfIslands.py)
    - Leetcode link: [https://leetcode.com/problems/number-of-islands/description/ ](https://leetcode.com/problems/number-of-islands/description/)
    - 分析：这是一个经典的图遍历问题，主要有两种方法：DFS和BFS。
    - geeksforgeeks solution (Union-Find): [https://www.geeksforgeeks.org/find-the-number-of-islands-set-2-using-disjoint-set/ ](https://www.geeksforgeeks.org/find-the-number-of-islands-set-2-using-disjoint-set/)
    - geeksforgeeks solution (DFS): [https://www.geeksforgeeks.org/find-number-of-islands/ ](https://www.geeksforgeeks.org/find-number-of-islands/)
- [Nodes at even distance](NodesAtEvenDistance.cpp)
- [Reconstruct Itinerary](ReconstructItinerary.cpp)
    - 思考过程：这是一道起始点确定的图遍历问题，需要访问所有的边一次。选择边的偏好在于字母序。假设给定N个顶点，E条边，可以首先从起始点为S的边里选出字母序较小的，然后再从与之相连的顶点里选择字母序小的，其中需要记录哪些边已经被使用掉。此题转化为：已知图中存在欧拉路径，如何找到一个路径？欧拉路径的经典算法Hierholzer.
    ```python
    path = []

    DFS(u):
        while (u存在未被访问的边e(u, v)）
            mark边e(u, v)为访问
            DFS(v)
        path.pushLeft(u)
    ```
    - 解题思路：构造好图以后，从JFK开始做DFS，最后将path返回就可以了。
