"""
Supports two operations:
- Union
- Find

It should be online algorithm.
"""

import unittest


class DisjointSetByArray(object):
    def __init__(self, N):
        self._id = list(range(N))
        self._rank = [0] * N
        self._count = N

    def union(self, x, y):
        """
            merge into one set that contains element x and
            the set that contains element (x and y are in
            different sets). The original sets will be destroyed.
        """
        id = self._id
        rank = self._rank
        i = self.find(x)
        j = self.find(y)

        if i == j:
            return

        self._count -= 1
        # Weighted union
        if self._rank[i] < self._rank[j]:
            id[i] = j
        elif self._rank[i] > self._rank[j]:
            id[j] = i
        else:
            id[j] = i
            rank[i] += 1

    def find(self, x):
        """
             returns the representative or a pointer to the representative of the set that contains element x.
        """
        id = self._id
        while x != id[x]:
            x = id[x] = id[id[x]]  # Path compression
        return x

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_rank(self):
        return self._rank


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.repr = None

    def set_repr(self, repr):
        self.repr = repr

    def set_next(self, next):
        self.next = next


class DisjointSetByTree(object):
    def __init__(self, N):
        pass

    def union(self, a, b):
        pass

    def find(self, x):
        pass


if __name__ == '__main__':
    #unittest.main()
    s = DisjointSetByArray(10)
    print s.find(1)
    print s.find(2)
    print s.find(3)
    s.union(1, 2)
    s.union(1, 3)
    print "after union"
    print s.find(2)
    print s.find(3)
    print s.get_rank()