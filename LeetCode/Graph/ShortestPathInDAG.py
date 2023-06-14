"""
Question
https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-undirected-graph
"""

#Approach
"""
--> BFS 
--> The neighbouring nodes that we encounter for the first time will not be it's shortest path because
weight of all the edges are different
--> We wil calculate the distance at each node.
--> If we encounter a path where the distance is shorter than the previous one, then we will re-calculate the
shortest path of it's neighbour by pushing into the heap  

"""

#Code
from typing import List
import heapq
class Solution:
    def shortestPath(self, N : int, M : int, edges : List[List[int]]) -> List[int]:
        INF = 10 ** 20
        adj = [[] for _ in range(N)]
        for u, v, dist in edges:
            adj[u].append([v, dist])
        
        shortPaths = [INF] * N
        heap = []
        heapq.heappush(heap, (0, 0))
        while heap:
            u, dist = heapq.heappop(heap)
            if dist < shortPaths[u]:
                shortPaths[u] = dist
                for v, nextDist in adj[u]:
                    heapq.heappush(heap, (v, dist + nextDist))
        
        for i, val in enumerate(shortPaths):
            if val == INF:
                shortPaths[i] = -1
        return shortPaths
        