'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to find the number of connected components in an undirected graph.

BFS? DFS? Union-find?
'''

class UnionFind(object):
    def __init__(self, n):
        self.id = [i for i in range(n)]
    
    def union(self, i, j):
        pid, qid = self.root(i), self.root(j)
        self.id[pid] = qid

    def connected(self, i, j):
        return self.root(i) == self.root(j)

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

class Solution(object):
    def countComponents(self, n, edges):
        uf = UnionFind(n)
        for e1, e2 in edges:
            uf.union(e1, e2)
        
        root_set = set()
        for i in range(n):
            root_set.add(uf.root(i))
        
        return len(root_set)


if __name__ == '__main__':
    sol = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(sol.countComponents(n, edges))