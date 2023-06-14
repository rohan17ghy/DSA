"""
Question
https://www.interviewbit.com/problems/cycle-in-undirected-graph/
GFG question test case can give some error
"""

#Approach
"""
--> Doing a DFS with visited array and tracking the parent at each recursion
--> Here visited is needed and we can't modify the node values to make it visited
bcoz we are doing some calc with parent in the child recursive call
"""

#Code
import collections
class Solution:    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		#Code here
        visited = [0] * V
        def isCycle(node, parent):
            if(visited[node]):
                return False
            
            visited[node] = 1
            ans = 0
            for v in adj[node]:
                if(not visited[v]):
                    if(isCycle(v, node)): return True
                elif(v != parent):
                    return True
                   
            return False
        
        
        for i in range(V):
            if(not visited[i] and isCycle(i, -1)):
                return True
        return False