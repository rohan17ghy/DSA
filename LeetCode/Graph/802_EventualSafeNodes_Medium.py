"""
Question
https://leetcode.com/problems/find-eventual-safe-states/description/
"""

#Approach
"""
--> One observation is that terminal nodes themselves are safe nodes
--> So we can start at terminal nodes and find all other safe nodes using topo sort
--> We need to create a different type of adjacency list
--> incAdj[u] for u means that there is a edge from u ---> incAdj[u]     
"""

#Code
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        #incAdj gives the nodes which are incoming to a particular node 
        #outEdges is the count of outgoing edge for a node 
        incAdj = [[] for _ in range(N)]
        outEdges = [0] * N
        for u in range(N):
            for v in graph[u]:
                incAdj[v].append(u)
                outEdges[u] += 1

        #Modified Topo Sort for outgoing edges
        q = collections.deque([])
        for i, outEdge in enumerate(outEdges):
            if outEdge == 0:
                q.append(i)

        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for u in incAdj[curr]:
                outEdges[u] -= 1
                if outEdges[u] == 0:
                    q.append(u)
        ans.sort()            
        return ans  
        