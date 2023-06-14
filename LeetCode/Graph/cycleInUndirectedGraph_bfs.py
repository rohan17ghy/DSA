"""
Question
https://www.interviewbit.com/problems/cycle-in-undirected-graph/
GFG question test case can give some error
"""

#Approach
"""
--> Doing a BFS and tracking the parent at each level of traversal
--> If the neighbouring node is already visited but it is not the parent node, that means there is 
a cycle
"""

#Code
import collections
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj = [[] for i in range(A+1)]
        visited = [False] * (A+1)
        
        for edge in B:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])        
        
        
        def isCycleBFS(node):    
            q = collections.deque([])            
            q.append((node, -1))
            while q:
                node, parent = q.popleft()
                visited[node] = True
                for i in adj[node]:
                    if(visited[i] and parent != i):
                        return True
                    if not visited[i]:
                        q.append((i, node))
            return False
        
        for i in range(len(adj)):
            if not visited[i] and isCycleBFS(i):
                return 1
        return 0