## How to find a solution

[https://www.topcoder.com/community/data-science/data-science-tutorials/how-to-find-a-solution/](https://www.topcoder.com/community/data-science/data-science-tutorials/how-to-find-a-solution/)

## Test

- **Edge cases**: Remember that "Constraints" section that we filled in? It's going to come in very handy. Design cases that make sure the code works when the min and/or max values of the constraints are hit. This includes negative numbers, empty arrays, empty strings, etc.
- Cases where there's **no solution**: To make sure the code does the right thing (hopefully you know what it is)
- **Non-trivial functional tests**: these depend very much on the problem. They would test the internal logic of the solution to make sure the algorithm works correctly.
- **Randomized tests**: this makes sure your code works well in the "average" case, as opposed to only working well on human-generated tests (where there's inherent bias).
- **Load testing**: Test your code with as much data as allowed by the constraints. These test your code against being very slow or taking up too much memory.

A good "test set" is a well-balanced combination of the above types. It will include tests that cover most edge cases, a few non-trivial functional tests, and then a series of random tests. 

Typically, we stay away from randomized tests and load tests during interviews, for obvious reasons. Instead, we like choosing a small-scale version of a non-trivial functional test, to make sure the code does the right thing. Then, we look at how the code would react to several edge cases, and finally think about whether the code would work well if no solution can be found.

This combination (non-trivial functional + edge + no solution) tends to be the most effective. For the amount of time it takes to design the tests and to run them on your code on a sheet of paper, it gives you the highest certainty in your code.

## Questions

### Arrays
- **Meet at the intersection**
    - Description: A map of streets is given, which has the shape of a rectangular grid with N columns and M rows. At the intersections of these streets there are people. They all want to meet at one single intersection. The goal is to choose such an intersection, which minimizes the total walking distance of all people. Remember that they can only walk along the streets (the so called "Manhattan distance").
- **Parking Lot Problem**
    - Description: There are N+1 parking spots, numbered from 0 to N. There are N cars numbered from 1 to N parked in various parking spots with one left empty. Reorder the cars so that car #1 is in spot #1, car #2 is in spot #2 and so on. Spot #0 will remain empty. The only allowed operation is to take a car and move it to the free spot.
- **Data Structure Design**
    - Description: Design a data structure, which supports several operations: insert a number with O(logN), return the median element with O(1), delete the median element with O(logN), where N is the number of elements in the data structure.
- **Palindrome Generation**
    - Description: Generate all palindromes using a set of N latin letters. 
- **Jump over numbers**
- **Digit Sum**
- **Numeric Palindromes**

### Dynamic Programming

- **Longest Increasing Subsequence**
    - solution: [https://www.hiredintech.com/classrooms/algorithm-design/lesson/12/task/14/solution](https://www.hiredintech.com/classrooms/algorithm-design/lesson/12/task/14/solution)
- **Count the paths**
    - solution: [https://www.hiredintech.com/classrooms/algorithm-design/lesson/12/task/15/solution](https://www.hiredintech.com/classrooms/algorithm-design/lesson/12/task/15/solution)

### Sorting

- Selection Sort, BubbleSort, Quick Sort, Merge Sort, Heap Sort
- **Sort the files**
- **Tasks Optimization**
- **Cover the Order**

### Math

- Representing numbers in different bases
- Integer number factorization
- Prime numbers
- Greatest common divisor (GCD)

### String

- *Rabin-Karp algorithm*
- *Knuth-Morris-Pratt algorithm*

### Graph Theory

```
def dfs(node)
    mark node as visited

    for next_node in neighbors(node)
        if not visited(next_node)
            dfs(next_node)
        end
    end
end
```
If implementing it recursively you need to be aware of the stack depth. The time complexity of DFS is *O(m)* where *m* is the number of edges.

With BFS the solution is usually implemented using a queue and is iterative.
There is one very useful effect of running BFS - when starting from a given node, it will get to all reachable nodes with the minimum possible number of hops (edges). This is useful in problems in which one needs to find the minimum path in terms of edges between two or more nodes in a graph.

```
def bfs(node)
  queue.add(node)
  mark node as visited
  distance[node] = 0

  while not queue.empty
    top_node = queue.pop
    for next_node in neighbours(top_node)
      if not visited(next_node)
        queue.add(next_node)
        mark next_node as visited
        distance[node] = distance[top_node] + 1
      end
    end
  end
end
```
The time complexity of BFS is O(m) where m is the number of edges in the graph.
