"""
Question
https://practice.geeksforgeeks.org/problems/steps-by-knight5927/1
"""

#Approach
"""
--> Apply 'Shortest path in undirected graph with unit weight' algo 
"""

#Code
import collections
class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		#Code here
		def isSafe(row, col):
		    return row >= 0 and row < N and col >= 0 and col < N    
		
		INF = 10 ** 20
		rowMoves = [2, 2, -2, -2, -1, 1, -1, 1]
		colMoves = [-1, 1, -1, 1, 2, 2, -2, -2]
		
		dist = [[INF for j in range(N)] for i in range(N)]
		q = collections.deque()
		q.append((KnightPos[0]-1, KnightPos[1]-1, 0))
		dist[KnightPos[0]-1][KnightPos[1]-1] = 0
		
		while(len(q) > 0):
		    row, col,  currDist = q.popleft()
		    for dx, dy in zip(rowMoves, colMoves):
		        nextRow, nextCol = row+dx, col+dy
		        if(isSafe(nextRow, nextCol)):
		            if(dist[nextRow][nextCol] == INF):
		                q.append((nextRow, nextCol, currDist + 1))
    		        dist[nextRow][nextCol] = min(currDist + 1, dist[nextRow][nextCol])
		
		if(dist[TargetPos[0]-1][TargetPos[1]-1] == INF):
		    return -1
		else:
		    return dist[TargetPos[0]-1][TargetPos[1]-1]