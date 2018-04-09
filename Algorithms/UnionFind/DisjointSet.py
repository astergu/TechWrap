"""
Supports two operations:
- Union
- Find

It should be online algorithm.
"""


class DisjointSetByArray(object):
    def __init__(self):
        self._disjoint_set = []

    def create_set(self, x):
        """
            creates a new set with one element {x}.
        """
        self._disjoint_set[x] = x

    def union(self, x, y):
        """
            merge into one set that contains element x and
            the set that contains element (x and y are in
            different sets). The original sets will be destroyed.
        """
        if self._disjoint_set[x] < self._disjoint_set[y]:
            self._disjoint_set[x] = self._disjoint_set[y]
        else:
            self._disjoint_set[y] = self._disjoint_set[x]

    def find(self, x):
        """
             returns the representative or a pointer to the representative of the set that contains element x.
        """
        if self._disjoint_set[x] < 0:
            return x
        else:
            self._disjoint_set[x] = self.find(self._disjoint_set[x])
            return self._disjoint_set[x]


class DisjointSetByTree(object):
    def union(self, a, b):
        pass

    def find(self, a, b):
        pass