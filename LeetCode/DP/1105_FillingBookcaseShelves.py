"""
Question
https://leetcode.com/problems/filling-bookcase-shelves/
"""

#Approach
"""
See the nore that the books can be places in the same order. This changes the problem completely and makes it much easier

DP approach. The intuition is that at every index i, books[i] be can either added to the current shelf or start a new shelf

TC: O(N^2), SC:O(N^2)
"""



"""
This code can be more cleaner
"""

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        N = len(books)
        INF = 10 ** 20

        dp = [0] * N

        #minHeight of shelfs for books[index:] with new shelf starting from index
        def findMin(index):
            if dp[index] > 0:
                return dp[index]
            
            if index == N-1:
                dp[index] = books[index][1]
                return dp[index]
            
            #New shelf is created at index i, place books in this
            """
            Two Options: 
                -> Either keep a book on this shelf OR
                -> Start a new shelf
            """ 
            currWidth, maxHeight = books[index]
            ans = INF
            for j in range(index + 1, N):
                if currWidth + books[j][0] <= shelfWidth:
                    #Not adding to current shelf
                    ans = min(ans, maxHeight + findMin(j))

                    #Adding to current shelf
                    currWidth += books[j][0]
                    maxHeight = max(maxHeight, books[j][1])                    
                else:
                    ans = min(ans, maxHeight + findMin(j))
                    break
                
                #Case when all books are added to shelf starting with books[index]
                if j == N-1:
                    ans = min(ans, maxHeight)

            dp[index] = ans
            return dp[index]
       
        var =  findMin(0)
        return var

        