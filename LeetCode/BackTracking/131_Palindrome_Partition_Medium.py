"""
Question
https://leetcode.com/problems/palindrome-partitioning/description/
"""
#Approach
"""
--> Explore all possible partitions with backtracking
--> OPTIMIZATION: The palindrome check for a substring can be memoized

TC: O(N * 2 ^ N), N for palindrome check and 2 ^ N for bactracking. How 2 ^ N ??? Check out time complexity
of backtracking at .\index.txt
SC: O(N ^ 2) for memoization

"""

#Code
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        
        #Memoizing the isPalindrome function
        palindromeRes = {}
        def isPalindrome(s, start, end):
            if start > end:
                return False

            if (start, end) in palindromeRes:
                return palindromeRes[(start, end)]

            while start <= end:
                if s[start] != s[end]:
                    palindromeRes[(start, end)] = False
                    return palindromeRes[(start, end)]
                start += 1
                end -= 1 

            palindromeRes[(start, end)] = True
            return palindromeRes[(start, end)]
        
        ans = []
        def palindromePartition(s, i, partition):
            if i >= N:
                ans.append(partition[:])
                return

            for k in range(i, N):
                if isPalindrome(s, i, k):
                    partition.append(s[i:k+1])
                    palindromePartition(s, k+1, partition)
                    partition.pop()
        
        palindromePartition(s, 0, [])
        return ans

