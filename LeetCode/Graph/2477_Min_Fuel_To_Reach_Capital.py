"""
Question
https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/
"""

#Approach
"""
--> DFS
--> Here the key point is to assume wat the recursive dfs function should return and lets assume it returns
that then how do we proceed. --> Recursive leap of faith
--> PATTERN: Recursive leap of faith

Reference: https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/solutions/2831660/dfs/

"""

#Code
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = collections.defaultdict(list)
        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False] * len(adj)
        if len(adj) == 0:
            return 0

        #Returns the number of visitors who are in a partially filled car
        #Also Returns the petrol used up by the node's childrens
        def dfs(node, depth):
            visited[node] = True
            riders, petrol = 0, 0
            for neigh in adj[node]:
                if not visited[neigh]:
                    curr_riders, curr_petrol = dfs(neigh, depth + 1)
                    riders += curr_riders
                    petrol += curr_petrol
            
            if node == 0:
                return 0, petrol
            
            #Adding 1 for the current city
            riders += 1
            
            #(riders // seats) * depth is the fuel for the car going all the way to the capital city
            petrol += ((riders // seats) * depth) + (1 if riders % seats > 0 else 0)
            riders = riders % seats
            
            return riders, petrol
        
        riders, petrol = dfs(0, 0)
        return petrol

