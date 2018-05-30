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
    - *Representation*: three ways to represent a graph in memory (objects and pointers, matrix, adjacency list), familiarize yourself with each representation and its pros and cons.
        - [*adjacency list*](../../Algorithms/Graph/Graph.h): 灵活，可适用于weighted graph，但是如果需要得知两个点(v, w)是否存在边，必须遍历Adj[v]. 
            - **Space complexity**: O(V+E)
            - **Time**: to list all vertices adjacent to *u*: \theta (degree(*u*)).
            - **Time**: to determine if (*u*, *v*) exists: O(degree(*u*)).
        - *adjacency matrix*: O(1)访问时间，但是需要V*V的memory，与边的多少无关。
            - **Space**: \theta (V^2)
            - **Time**: to list all vertices adjacent to *u*: \theta (V).
            - **Time**: to determine if (*u*, *v*) exists: \theta (1).
            -
    - distance, search, connectivity, cycle-detection

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

