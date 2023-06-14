"""
Question
https://leetcode.com/problems/path-with-minimum-effort/
"""

#Approach
"""
--> A simple approach is to use Djikstra's algo whose TC: O(E*log(V)) which in this
problem is O(M*N*log(M*N))
--> PATTERN: Another approach is to binary search the answer and use BFS.
Time Complexity of BFS is O(V + E) which in this problem is O(M*N + 4*M*N) and binary
search is O(log(MAX_HEIGHT)) = O(M*N*log(MAX_HEIGHT))

--> Depending on the inputs we can either use Djikstra's or BFS(with binary search)

Reference: https://leetcode.com/problems/path-with-minimum-effort/discuss/909017/JavaPython-Dijikstra-Binary-search-Clean-and-Concise
"""

#Code
#Approach: Djikstra's

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        N = len(heights)
        M = len(heights[0])
        INF = 10 ** 20
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        def isSafe(row, col):
            if(row < 0 or row >= N):
                return False
            if(col < 0 or col >= M):
                return False
            return True
            
        
        effort = collections.defaultdict(lambda : INF)
        minHeap = []
        heapq.heappush(minHeap, (0, 0, 0))
        #effort[(0, 0)] = 0
        
        while(len(minHeap) > 0):
            d, row, col = heapq.heappop(minHeap)
            if(d < effort[(row, col)]):
                effort[(row, col)] = d
                for dx, dy in direct:
                    if(isSafe(row+dx, col+dy)):
                        heapq.heappush(minHeap, (max(d, abs(heights[row][col]-heights[row+dx][col+dy])), row+dx, col+dy))
        #print(effort)
        return effort[(N-1,M-1)]