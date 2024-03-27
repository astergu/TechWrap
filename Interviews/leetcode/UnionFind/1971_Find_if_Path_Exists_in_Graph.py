'''
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
'''

from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vertices = [x for x in range(n)]
        
        def root(i):
            nonlocal vertices
            while i != vertices[i]:
                vertices[i] == vertices[vertices[i]]
                i = vertices[i]
            return i
            
        def union(u, v):
            nonlocal vertices
            i, j = root(u), root(v)
            vertices[i] = j

        def connected(u, v):
            return root(u) == root(v)

        for e in edges:
            union(e[0], e[1])
        
        print(vertices)
        return connected(source, destination)


if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination = 5
    print(sol.validPath(n, edges, source, destination))