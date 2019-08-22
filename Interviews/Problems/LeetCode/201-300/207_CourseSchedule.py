"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

Note:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.


"""


class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for x, y in prerequisites:
            degree[x] += 1
            graph[y].append(x)

        flag = True
        courses = list(range(numCourses))
        while flag and courses:
            flag = False
            remove = []
            for x in courses:
                if degree[x] == 0:
                    for succ in graph[x]:
                        degree[succ] -= 1
                    remove.append(x)
                    flag = True
            for x in remove:
                courses.remove(x)

        return len(courses) == 0


if __name__ == '__main__':
    s = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    print(s.canFinish(numCourses, prerequisites))
