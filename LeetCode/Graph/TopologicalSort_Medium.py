"""
Question
https://practice.geeksforgeeks.org/problems/topological-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=topological-sort
"""

#Approach
"""
--> We assume that graph is a DAG and topo sort is possible, so we don't need to take care of cycles
--> DFS

"""

#Code
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        def dfs(u, stack):
            if vis[u]:
                return
            
            vis[u] = True
            for v in adj[u]:
                if not vis[v]:
                    dfs(v, stack)
            stack.append(u)        
        
        stack = []        
        vis = [False] * V
        for i in range(V):
            if not vis[i]:
                dfs(i, stack)
        
        stack.reverse()
        return stack

        