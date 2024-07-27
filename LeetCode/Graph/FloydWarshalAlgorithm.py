"""
Question
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
"""

#Approach
"""
Floyd Warshal Algorithm. Similar to DP
The logic is if we consider 3 nodes A, B, C then
distance(A, B) = min(distance(A, B), distance(A, C) + distance(C, B))
"""

class Solution:
    def findTheCity(self, N: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = 10 ** 20
        dis = [[INF] * N for _ in range(N)]
        for u, v, w in edges:
            dis[u][v], dis[u][u] = w, 0
            dis[v][u], dis[v][v] = w, 0
        
        #Floyd Warshal Algorithm. Similar to DP
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        
        best_city = None
        best_cities = INF
        for i in range(N):
            reachable = 0
            for j in range(N):
                if dis[i][j] <= distanceThreshold:
                    reachable += 1
            
            if reachable <= best_cities:
                best_cities = reachable
                best_city = i
        return best_city