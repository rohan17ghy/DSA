

## Read input as specified in the question.
## Print output as specified in the question.

class Solution:
    def all_longest_common_subsequences(self, text1, text2):
        N1, N2 = len(text1), len(text2)
        R, C = N1, N2

        #Creating the dp table with bottom up approach
        dp = [[-1] * (N2 + 1) for _ in range(N1 + 1)]
        for i in range(N1, -1, -1):
            for j in range(N2, -1, -1):
                if i >= N1 or j >= N2:
                    dp[i][j] = 0                
                elif text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # Function to rotate the matrix by 180 degree
        def reverseColumns(arr):
            for i in range(C):
                j = 0
                k = C-1
                while j < k:
                    t = arr[j][i]
                    arr[j][i] = arr[k][i]
                    arr[k][i] = t
                    j += 1
                    k -= 1
                    
        # Function for transpose of matrix
        def transpose(arr):
            for i in range(R):
                for j in range(i, C):
                    t = arr[i][j]
                    arr[i][j] = arr[j][i]
                    arr[j][i] = t
        
        # Function for display the matrix
        def printMatrix(arr):
            for i in range(R):
                for j in range(C):
                    print(arr[i][j], end = " ")
                print()
        
        def rotate180(arr):
            transpose(arr)
            reverseColumns(arr)
            transpose(arr)
            reverseColumns(arr)

        rotate180(dp)

        
        ans = []
        print(dp)
        #DP Path reconstruction
        def backTrackAll(C, X, Y, i, j):
            if i == 0 or j == 0:
                return set([""])
            elif X[i-1] == Y[j-1]:
                return set([Z + X[i-1] for Z in backTrackAll(C, X, Y, i-1, j-1)])
            else:
                R = set()
                if C[i][j-1] >= C[i-1][j]:
                    R.update(backTrackAll(C, X, Y, i, j-1))
                if C[i-1][j] >= C[i][j-1]:
                    R.update(backTrackAll(C, X, Y, i-1, j))
                return R
        
        #reconstruct(0, 0, [])
        #return ans
        return backTrackAll(dp, text1, text2, N1, N2)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        f = open("C:\\Users\\Debopriya\\Downloads\\fileInput.txt", mode="r")
        text1, text2 = "abaaa", "baabaca"      
        obj = Solution()
        res = obj.all_longest_common_subsequences(text1, text2)
        print(res)