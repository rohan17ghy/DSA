"""
Question
https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
"""

#Approach
"""
--> Recursive approach can be used.
--> When visiting a node, consider it in answer then recursively traverse the 
rest of the graph

TC: O(V + E) SC: O(V + E)
"""

#Code
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = set()
        ans = []
        def dfs(num, adj, visited, ans):
            if(num in visited):
                return
            
            neighbours = adj[num]
            ans.append(num)
            visited.add(num)
            for neighbour in neighbours:
                dfs(neighbour, adj, visited, ans)
        
        
        dfs(0, adj, visited, ans)
        return ans