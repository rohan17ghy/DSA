"""
Question
https://www.codingninjas.com/codestudio/problems/longest-route_1170525?leftPanelTab=0
"""
#Approach
"""
--> Explore all possible paths thorugh recursion
--> One edge case needs to be taken care which is if the source is itself a blocked cell
--> If source is blocked cell than the assumption is we can't move from a blocked cell. Return -1  
"""
#TC: O(4 ^(n*m)) SC: O(n*m)
 
def longestpath(n, m, mat, sx, sy, dx, dy):
    #Handling this special case when the source itself is a blocked cell
    #Here the assumption is we can't move from a blocked cell
    if(mat[sx][sy] == 0):
        return -1
    
    visited = [[0 for j in range(m)] for i in range(n)]
    ans = solve(n, m, mat, sx, sy, dx, dy, visited)
    if(ans < 0):
        return -1
    return ans
    
def solve(n, m, mat, i, j, dx, dy, visited):
    if(i == dx and j == dy):
        return 0
    
    rowNum = [-1, 1, 0, 0]
    colNum = [0, 0, -1, 1]
    
    ans = float('-inf')
    visited[i][j] = 1
    for k in range(4):
        if(isSafe(n, m, mat, i+rowNum[k], j+colNum[k], visited)):
            ans = max(ans, 1 + solve(n, m, mat, i+rowNum[k], j+colNum[k], dx, dy, visited))
    visited[i][j] = 0        
    return ans    
    

def isSafe(n, m, mat, i, j, visited):
    if(i < 0 or i >= n):
        return False
    if(j < 0 or j >= m):
        return False
    if(mat[i][j] == 0 or visited[i][j] == 1):
        return False
    return True
