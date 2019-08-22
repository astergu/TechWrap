"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .

Note:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.


"""


class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        degree = [[_, 0] for _ in range(numCourses)]
        for x, y in prerequisites:
            degree[x][1] += 1
            graph[y].append(x)

        courses = list(range(numCourses))
        degree_dict = dict(degree)
        sorted_degree = sorted(degree, key=lambda x: x[1], reverse=True)
        ret = []
        while courses:
            first = sorted_degree.pop()
            if first[1] != 0:
                return []
            ret.append(first[0])
            courses.remove(first[0])
            del degree_dict[first[0]]
            for x in graph[first[0]]:
                degree_dict[x] = degree_dict[x] - 1
            sorted_degree = sorted(
                degree_dict.items(), key=lambda x: x[1], reverse=True)

        return ret

    def topSolution(self, numCourses, prerequisites):
        import collections import defaultdict
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        path = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, path):
                return []
        return path

    def dfs(self, graph, visited, i, path):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j, path):
                return False
        visited[i] = 2
        path.append(i)
        return True


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    s = Solution()
    print(s.findOrder(numCourses, prerequisites))
