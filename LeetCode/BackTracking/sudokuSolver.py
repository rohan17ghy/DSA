"""
Question
https://practice.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1
"""

#Approach: 
"""
--> For every empty cell try with all possible number from 1 to 9
--> Before adding a number to grid[i][j] check if it is safe to insert that num
--> Safe means it should not violate the rules of sudoku
--> Formula grid[3*(row//3) + i//3][3 * (col//3) + i % 3] 
"""
#TC: O(9 ^ m) --> where m is no. of empty cells
#SC: O(1)

class Solution:
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        return self.solve(grid)
        
    def solve(self, grid):
        for i in range(9):
            for j in range(9):
                if(grid[i][j] != 0):
                    continue
                
                for num in range(1, 10):
                    if(self.isSafe(grid, num, i, j)):
                        grid[i][j] = num
                        isSolved = self.solve(grid)
                        if(isSolved):
                            return True
                        grid[i][j] = 0
                return False
        
        return True
                    
            
    def isSafe(self, grid, num, row, col):
        for i in range(9):
            #Checking the num in row
            if(grid[row][i] == num):
                return False
            
            #Checking the num in col
            if(grid[i][col] == num):
                return False
            
            #Checking the num in 3x3 matrix
            #Need to remember the formula
            if(grid[3*(row//3) + i//3][3 * (col//3) + i % 3] == num):
                return False
        
        return True
        
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end = " ")