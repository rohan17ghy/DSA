"""
Question
https://leetcode.com/problems/longest-cycle-in-a-graph/description/
"""

#Approach
"""
#Approach1:
--> We can use the concept of dfsVisited, i.e we track the nodes that are visited in the current dfs recursion
--> We use dfsVisited and depth of each node to find the longest cycle

TC: O(N), SC: O(N)  

#Approach2:
--> Another approach could be that of tortoise and hare algorithm used in linked list
--> This algo is used to find cycle in LinkedList

TC: O(N), SC:O(1)
"""

#Code
#Approach 1
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        N = len(edges)
        visited = [False] * N
        def dfs(node, depth, dfsVisited):
            if edges[node] == -1:
                visited[node] == True
                return -1
            
            if node in dfsVisited:
                return depth - dfsVisited[node]

            ans = -1            
            dfsVisited[node] = depth
            if not visited[edges[node]]:
                ans = dfs(edges[node], depth+1, dfsVisited)
            visited[node] = True
            return ans
        
        best = -1
        for i in range(N):
            if not visited[i]:
               best = max(best, dfs(i, 0, {}))
        return best 

        