"""
Question
https://practice.geeksforgeeks.org/problems/n-queen-problem0315/1
"""

#Approach: 
"""
--> Place the queen at every possible position and find the combinations so that it is non-attacking
--> Sounds like a brute force, but there is no other optimized approach for these knd of combination
problems   
"""
#TC: O(n!) SC: O(n^2)

class Solution:
    def nQueen(self, n):
        # code here
        visited = [[0 for j in range(n)] for i in range(n)]
        pos = [0] * n
        ans = []
        self.nQueenHelper(n, visited, 0, pos, ans)
        #ans.sort()
        return ans
        
    
    def nQueenHelper(self, n, visited, j, pos, ans):
        #Base cases
        if(j >= n):
            ans.append(pos.copy())
            return
        
        
        for i in range(n):
            if(self.isSafe(visited, i, j)):
                visited[i][j] = 1
                pos[j] = i + 1
                self.nQueenHelper(n, visited, j + 1, pos, ans)
                pos[j] = 0
                visited[i][j] = 0
    
    def isSafe(self, visited, row, col):
        #Check for all rows before current
        i = row
        j = col
        while(j >= 0):
            if(visited[i][j] == 1):
                return False
            j -= 1
            
        #Check for upper left diagonal
        i = row
        j = col
        while(i >= 0 and j >= 0):
            if(visited[i][j] == 1):
                return False
            i -= 1
            j -= 1
        
        
        #Check for lower left diagonal
        i = row
        j = col
        while(i < n and j >= 0):
            if(visited[i][j] == 1):
                return False
            i += 1
            j -= 1
        
        return True 


#Approach 1 optimized:
"""
--> In the isSafe() of the above approach we are using O(n) every time. So the time complexity is 
actually O(n! * n) which is O(n!)
--> But this O(n) TC can be reduced such that isSafeworks in O(1)
--> Refer hard copy notes for the optimization  
"""
