"""
Question
https://leetcode.com/problems/course-schedule-ii/description/
"""

#Approach
"""
--> Kahn algorithm
"""

#Code
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        N = numCourses

        #Creating adjacency list
        adj = [[] for _ in range(N)]
        for v, u in prerequisites:
            adj[u].append(v)
        
        #Topo Sort
        incEdges = [0] * N
        for u in range(N):
            for v in adj[u]:
                incEdges[v] += 1
        
        q = collections.deque([])
        for i, inc in enumerate(incEdges):
            if inc == 0:
                q.append(i)
        
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for v in adj[curr]:
                incEdges[v] -= 1
                if incEdges[v] == 0:
                    q.append(v)
        
        if len(ans) < N:
            return []
        return ans
        