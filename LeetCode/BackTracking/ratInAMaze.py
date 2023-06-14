"""
Question
https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
"""

#Approach:
"""
--> Explore all possible paths
--> If some path successfully reaches the destination then add that to result
--> There is no easier way to do it, time complexity will be exponential

--> Follow Up: Can we use memoization here. Store all the (i, j) coordinates from
where we can't reach to the answer ??   
"""
#TC: O(4^(N^2)), SC: O(N ^ 2)

class Solution:
    
    def findPath(self, m, n):
        # code here
        ans = []
        visited = [[0 for j in range(n)] for i in range(n)]
        self.findPathHelper(m, n, visited, 0, 0, [], ans)
        return ans
        
    def findPathHelper(self, m, n, visited, i, j, path, ans):
        if(i == n-1 and j == n-1):
            ans.append(''.join(path))    
            return
        
        if(m[i][j] != 0 and visited[i][j] != 1):
            #Lexicographical Order: Down Left Right Up
            #Down
            if(self.isSafe(m, n, visited, i + 1, j)):
                visited[i][j] = 1
                path.append("D")
                self.findPathHelper(m, n, visited, i + 1, j, path, ans)
                path.pop()
                visited[i][j] = 0
            
            #Left
            if(self.isSafe(m, n, visited, i, j-1)):
                visited[i][j] = 1
                path.append("L")
                self.findPathHelper(m, n, visited, i, j-1, path, ans)
                path.pop()
                visited[i][j] = 0
            
            #Right
            if(self.isSafe(m, n, visited, i, j + 1)):
                visited[i][j] = 1
                path.append("R")
                self.findPathHelper(m, n, visited, i, j+1, path, ans)
                path.pop()
                visited[i][j] = 0
            
            #Up
            if(self.isSafe(m, n, visited, i - 1, j)):
                visited[i][j] = 1
                path.append("U")
                self.findPathHelper(m, n, visited, i - 1, j, path, ans)
                path.pop()
                visited[i][j] = 0
            
            
        
            
    def isSafe(self, m, n, visited, newI, newJ):
        if((newI >= 0 and newI < n) and (newJ >= 0 and newJ < n) and visited[newI][newJ] == 0 and m[newI][newJ] == 1):
            return True
        return False    