[**Disjoint Set Implementation**](DisjointSet.py)
    - **Array(数组实现)**: 用array来表示输入中每个元素的group，比如名为parent，其中parent[i]代表每个元素的group。这种实现union操作复杂度为O(n)，find操作复杂度为O(1)。
    - **Tree(树实现)**：在同一棵树里的元素代表他们在同一个组（disjoint set）里，其中每棵树的根节点叫做the representative of the set。这种实现union操作复杂度为O(1)，find操作复杂度为O(n)。

## Questions
- [Number of Islands](NumberOfIslands.py)
    - Leetcode link: [https://leetcode.com/problems/number-of-islands/description/](https://leetcode.com/problems/number-of-islands/description/)
    - geeksforgeeks solution (Union-Find): [https://www.geeksforgeeks.org/find-the-number-of-islands-set-2-using-disjoint-set/](https://www.geeksforgeeks.org/find-the-number-of-islands-set-2-using-disjoint-set/)
    - geeksforgeeks solution (DFS): [https://www.geeksforgeeks.org/find-number-of-islands/](https://www.geeksforgeeks.org/find-number-of-islands/)


## References
- [https://www.topcoder.com/community/data-science/data-science-tutorials/disjoint-set-data-structures/](https://www.topcoder.com/community/data-science/data-science-tutorials/disjoint-set-data-structures/)