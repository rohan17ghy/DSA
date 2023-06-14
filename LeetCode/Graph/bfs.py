"""
Question
https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
"""

#Approach
"""
--> Traverse through the neighbouring nodes of the current node and append it in 
the queue.
--> Maintain the nodes which are already visited using a set

TC: O(V + E) SC: O(V + E) 
"""

#Code
import collections
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        q = collections.deque()
        q.append(0)
        
        visited = set()
        ans = []
        while(len(q) > 0):
            num = q.popleft()
            if(num in visited):
                continue
            neighbours = adj[num]
            for i in range(len(neighbours)):
                if(neighbours[i] not in visited):
                    q.append(neighbours[i])
            ans.append(num)
            visited.add(num)
        return ans