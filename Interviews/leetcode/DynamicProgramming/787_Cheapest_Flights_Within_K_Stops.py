'''
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
'''

from typing import List
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for flight in flights:
            adj[flight[0]].append(flight[1])


if __name__ == '__main__':
    sol = Solution()
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 
    src = 0
    dst = 3
    k = 1
    print(sol.findCheapestPrice(n, flights, src, dst, k))