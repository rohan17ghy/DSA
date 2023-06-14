#Code
class Solution:
    def printMatrix(self, mat):
        R = len(mat)
        C = len(mat)

        for i in range(R):
            for j in range(C):
                print(mat[i][j], sep=' ')
            print('\n')

    def boundaryTraversal(self, mat):
        R = len(mat)
        C = len(mat[0])

        #Traversing first and last columns for all rows
        for i in range(R):
            for j in [0, C-1]:
                print(mat[i][j])
        
        #Traversing first and last row for all columns
        for i in [0, R-1]:
            for j in range(1, C-1):
                print(mat[i][j])

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol = Solution()
sol.printMatrix(mat)
sol.boundaryTraversal(mat)
