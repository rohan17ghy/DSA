"""
Question
https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=shortest-path-in-undirected-graph
"""

#Approach
"""
--> Djikstra's algorithm
--> We need to keep track of prev Node from where it arrived. If we are at 'v' node then keep track of 'u' node
from where it arrived
--> Then use Path reconstruction to construct the path     


"""

#Code
import heapq
class Solution:
    def shortestPath(self, N, M, edges):
        INF = 10 ** 20
        dist = [INF] * (N+1)
        prevNode = [-1] * (N+1)
        
        adj = [[] for _ in range(N+1)]
        for u, v, wt in edges:
            adj[u].append([v, wt])
            adj[v].append([u, wt])
        
        h = []
        heapq.heappush(h, (0, 1, -1))
        prevNode[1] = -1
        while h:
            currDist, node, prev = heapq.heappop(h)
            if currDist < dist[node]:
                dist[node] = currDist
                prevNode[node] = prev
                for nextNode, nextDist in adj[node]:
                    if currDist + nextDist < dist[nextNode]:
                        heapq.heappush(h, (currDist+nextDist, nextNode, node))
        
        #Path reconstruction
        stack = []
        curr = N
        while curr != 1:
            if curr == -1:
                return [-1]  
            stack.append(curr)
            curr = prevNode[curr]
            
        stack.append(curr)
        stack.reverse()
        return stack