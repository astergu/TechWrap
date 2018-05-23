[**Disjoint Set Implementation**](DisjointSet.py)
- **Definition(定义)**：a set of elements partitioned into a number of disjoint (non-overlapping) subsets.
- **Array(数组实现)**: 用array来表示输入中每个元素的group，比如名为parent，其中parent[i]代表每个元素的group。这种实现union操作复杂度为O(n)，find操作复杂度为O(1)。
- *Linked List(链表实现)*：
- **Tree(树实现)**：在同一棵树里的元素代表他们在同一个组（disjoint set）里，其中每棵树的根节点叫做the representative of the set。这种实现union操作复杂度为O(1)，find操作复杂度为O(n)。
- **优化**
    - **Path Compression (路径压缩)**
    - **Weighted Union (带权重的union)** 

## Questions


## References
- Disjoint-set data structure: [https://en.wikipedia.org/wiki/Disjoint-set_data_structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)
- MIT Courseware: [https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec16.pdf](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec16.pdf)
- [https://www.topcoder.com/community/data-science/data-science-tutorials/disjoint-set-data-structures/](https://www.topcoder.com/community/data-science/data-science-tutorials/disjoint-set-data-structures/)
