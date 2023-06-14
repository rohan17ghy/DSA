"""
Question
https://leetcode.com/problems/number-of-provinces/description/
"""

#Approach
"""
--> Converting the adjacency matrix to an adjacency list 
--> Using dfs to find the connected components
--> Finding the total number of connected components

TC: O(N) --> Looping through all nodes + O(V + 2E) --> DFS
SC: O(N) --> Visited array + O(N) --> Recursion stack space
"""

#Code
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        #Converting adjacency matrix to adjacency list
        adj = [[] for r in range(n)]
        for r in range(n):
            for c in range(n):
                if(isConnected[r][c] == 1 and r != c):
                    adj[r].append(c)
                    adj[c].append(r)
        
        def dfs(row):
            visited[row] = True
            for col in adj[row]:
                if(not visited[col]):
                    dfs(col)
        
        count = 0
        visited = [False] * n
        for row in range(n):
            if(not visited[row]):
                count += 1
                dfs(row)
        return count