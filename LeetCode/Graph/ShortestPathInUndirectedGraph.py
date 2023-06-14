"""
Question
https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-undirected-graph-having-unit-distance 
"""

#Approach
"""
--> BFS 
--> The neighbouring nodes that we encounter for the first time will be it's shortest path because
weight of all the edges are 1

"""

#Code
import collections
class Solution:
    def shortestPath(self, edges, N, M, src):
        adj = [[] for _ in range(N)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        shortPath = [-1] * N
        q = collections.deque([])
        q.append((src, 0))
        
        while q:
            u, dist = q.popleft()
            if shortPath[u] == -1:
                shortPath[u] = dist
                for v in adj[u]:
                    if shortPath[v] == -1:
                        q.append((v, dist+1))
        
        return shortPath
        