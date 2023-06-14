"""
Question
https://practice.geeksforgeeks.org/problems/topological-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=topological-sort
"""

#Approach
"""
--> Keep track of the incoming edges
--> Enter into queue when incoming edge becomes zero for a node
--> Traverse through immediate neighbours(BFS) and reduce the incoming edge(remove the edge)
--> Pop from queue and add to the answer because the incoming edge is zero

--> Reference: https://www.youtube.com/watch?v=73sneFXuTEg&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=22
"""

#Code
import collections
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
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
        return ans

        