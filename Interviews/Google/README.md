Google面试准备的试题。
## Topic Cover Plan
### Algorithms

CLRS

- **Binary Search**
- **BFS and DFS**
- **Sorting**
- **Divide-and-Conquer**
- **Dynamic Programming**
- **Greediness**
- **Recursion**
- **Others**
    - **Dijkstra**
    - **A***

### Data Structures

CLRS

*implement a range of data structures using an array (especially hash maps and hash tables)*

- **Array**
- **Linked List**
- **Hash Set**
- **Hash Map**
- **Hash Table**
- **Stack**
- **Queue**
- **Trees**
- **Heap**
- **Graph**
    - **Representation**: three ways to represent a graph in memory (objects and pointers, matrix, adjacency list), familiarize yourself with each representation and its pros and cons.
        - [*adjacency list*](../../Algorithms/Graph/Graph.h): 灵活，可适用于weighted graph，但是如果需要得知两个点(v, w)是否存在边，必须遍历Adj[v]. 
            - **Space complexity**: O(V+E)
            - **Time**: to list all vertices adjacent to *u*: \theta (degree(*u*)).
            - **Time**: to determine if (*u*, *v*) exists: O(degree(*u*)).
        - *adjacency matrix*: O(1)访问时间，但是需要V<sup>2</sup>的memory，与边的多少无关。
            - **Space**: \theta (V^2)
            - **Time**: to list all vertices adjacent to *u*: \theta (V).
            - **Time**: to determine if (*u*, *v*) exists: \theta (1).
    - **Traversal**
        - **Breadth-First Search (BFS)** [递归实现](../../Algorithms/Graph/Graph.cpp), [迭代实现](../../Algorithms/Graph/GraphUtil.cpp)
            - Prim和Dijkstra算法用了相似的思想。在BFS的同时会得到BF Tree，由此可以得到*v*到起始点*s*的距离。**Space Complexity**: O(V), **Time Complexity**: O(V+E). 因为BFS过程可以扫描得到其他顶点到起始点的距离，因此BFS可以**最短路径(Shortest Path)**。
            - BFS的应用：**Shortest Path and Minimum Spanning Tree for unweighted graph**, **Peer to Peer Networks**, **Crawlers in Search Engines**, **Social Networking Websites**, **GPS Navigation systems**, **Broadcasting in Network**, **Garbage Collection**, **Cycle detection in undirected graph** (both BFS and DFS can work for undirected graphs, but only DFS can work for directed graphs), **Ford-Fulkerson algorithm**, **To test if a graph is Bipartite**, **Path
                Finding**, **Finding all nodes within one connected component**.
                - check [this](https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/) for details.
        - **Depth-First Search (BFS)**: [递归实现](../../Algorithms/Graph/Graph.cpp), [迭代实现](../../Algorithms/Graph/GraphUtil.cpp)  DFS的特征之一是会显示出图的parenthesis结构，时间复杂度\theta (V + E)。如果只是检查邻接节点，那么从s出发无法连接到的点就无法遍历到，因此需要对每一个节点都调用dfs。
            - DFS的应用：**Detecting Cycle in a Graph**, **Path Finding**, **Topological Sorting**, **To test if a graph is bipartite**, **Finding Strongly Connected Components of a graph**, **Solving puzzles with only one solution, such as mazes** 
                - check [this](https://www.geeksforgeeks.org/applications-of-depth-first-search/) for details.
        - **什么时候用BFS，什么使用用DFS？**
        - **Topological Sort 拓扑排序**: [递归实现](../../Algorithms/Graph/TopologicalSort.cpp) 只有在有向无环图(DAG)上才存在TS。一张图上可能存在多个拓扑排序。拓扑排序的第一个点是入度为0的点。采用DFS，时间复杂度\theta (V+E)
    - **Connectivity 连通性**
        - **strongly connected component**: *V*的一个子集，在这个子集中，任意*u*和*v*是可以互相连通的。 


### Problem Solving

Programming Pearls

### System Design

Introduction to Information Retrieval

what Google is at its core

### Operation Systems

### Interesting Questions to answer in reading CLRS

1. The **transpose** of a directed graph G=(V, E) is the graph G<sup>T</sup>=(V, E<sup>T</sup>), that is, G<sup>T</sup> is G with all its edges reversed. Describe efficient algorithms for computing G<sup>T</sup> from G, for both the adjacency-list and adjacency-matrix representations of G. Analyze the running times of your algorithms.

## GeeksforGeeks Questions

- [SumOfBitDifferences](SumOfBitDifferences.cpp): 纯实现，考察代码一次完成度和速度。
- [Modular Exponentiation for large numbers](ModularExponentiationForLargeNumbers.cpp): 主要问题是如果简单实现，会引起overflow，因此需要考虑分治，把大数变成小数。
- [Rotate a 2D array without using extra space](Rotate2DArray.cpp) **[TODO]**
- [Find sum of different corresponding bits for all pairs](FindSumOfDifferentCorrespondingBitsForAllBits.cpp): 纯实现，利用异或+数1策略
- [Is Sudoku Valid](IsSudokuValid.cpp) **[TODO]**
- [X Total Shapes](XTotalShapes.cpp): 类似于LC上的Number of Islands。
-

## Glassdoor questions

