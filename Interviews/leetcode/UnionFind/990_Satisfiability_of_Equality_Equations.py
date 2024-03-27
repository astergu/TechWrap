'''
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".
Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

 

Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.

Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

'''
from typing import List

class UnionFind(object):
    def __init__(self):
        self.id = [i for i in range(26)]
        self.A = ord('a')

    def union(self, p, q):
        pid = self.root(ord(p) - self.A)
        qid = self.root(ord(q) - self.A)
        self.id[pid] = qid
    
    def connected(self, p, q):
        return self.root(ord(p) - self.A) == self.root(ord(q) - self.A)
    
    def root(self, i):
        while self.id[i] != i:
            i = self.id[i]
        return i

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        nq = [] # not-equal
        uf = UnionFind()

        for eq in equations:
            a, b = eq[0], eq[-1]
            print(a, b)
            if "!=" == eq[1:3]: # not equal
                nq.append((a, b))
            elif "==" in eq[1:3]: # equal
                uf.union(a, b)
        
        print(uf.id)

        for a, b in nq:
            if uf.connected(a, b):
                return False
        
        return True


if __name__ == '__main__':
    sol = Solution()
    equations = ["b==a","a==b"]
    print(sol.equationsPossible(equations))