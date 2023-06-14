"""
Question
https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-a-directed-graph
"""

#Approach
"""
--> Kahn algo can be used to generate topo sort
--> If the length of topo sort < V, where V is the total number of vertices than there is a cycle 
"""

#Code
import collections
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        # Code here
        incEdge = [0] * V
        for u in range(V):
            for v in adj[u]:
                incEdge[v] += 1
        
        q = collections.deque([])
        for u, inc in enumerate(incEdge):
            if inc == 0:
                q.append(u)
        
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for v in adj[curr]:
                incEdge[v] -= 1
                if incEdge[v] == 0:
                    q.append(v)
        
        if len(ans) < V:
            return 1
        return 0

        