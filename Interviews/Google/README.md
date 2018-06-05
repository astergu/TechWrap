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
- **Hash Table 哈希表**
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
        - **strongly connected component**: *V*的一个子集，在这个子集中，任意*u*和*v*是可以互相连通的。采用两个DFS分别在G和G<sup>T</sup>里查找.
            -
            基本思想：用第一次DFS把图中的节点按照叶节点到根节点的顺序压入栈中，也就是从某个节点所能达到的最深的节点先压入栈中，最后才是这个起始节点，也就是类似于拓扑排序的思想。接着，把整个图转置以后，所有的边指向反转。再把访问数组visited重置为false，把栈中的节点抛出，用这个节点去调dfs，如果是SCC，那么所有从这个节点反向可以访问得到的节点会依次被处理，直到这个SCC被完全处理。由此可以统计一张图中的SCC的组成以及个数。
    - **Search 查找**
        - **Minimum Spanning Trees 最小生成树**: Given connected, undirected graph *G* with positive edge weights, find a min weight set of edges that connects all of the vertices. [Prim algorithm]和[Kruskal algorithm]，如果用二叉堆，那么每个算法的时间复杂度胃O(ElgV)，如果用Fabonacci堆，那么Prim算法的时间复杂度可以到O(E+VlgV)。这两种算法是贪心算法。
        - **Single-Source Shortest Paths 单源最短路径**: Given a weighted, directed graph G=(V, E) and a source vertex in the graph, find the shortest paths from source to all vertices in the given graph. *BFS is a shortest path algorithm that works on unweighted graphs. 最短路径问题通常包含一个子结构，即两点之间的最短路径包含其他的最短字子路径。
            - [**Dijkstra算法**](../../Algorithms/Graph/Dijkstra.cpp)假设所有边的权重都是非负的(代码不保留path信息，但是可以通过增加一个parent数组来持续更新得到。该算法也可以用到有向图中。
                - 时间复杂度O(V<sup>2</sup>)，如果输入的图是邻接表表示的，复杂度可以通过二叉堆来降低到O(ElogV)).
            - [**Bellman-Ford算法**](../../Algorithms/Graph/BellmanFord.cpp)允许负权重的边，比Dijkstra更简单，而且更适合分布式系统。
                - 时间复杂度O(VE)
            - [**Floyd-Warshall算法**]
                - 时间复杂度：O(V<sup>3</sup>)
    - **Maximum Flow 最大流算法**
        
        
        
### Problem Solving

Programming Pearls

- [Circular Array With One Single Complete Cycle](CircularArrayWithCompleteCycle.cpp): a sample question in Google coaching session.

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

