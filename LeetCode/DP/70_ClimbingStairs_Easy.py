"""
Question
https://leetcode.com/problems/climbing-stairs/description/
"""

#Approach
"""
--> Need to figure out the sub problem and the recursion pattern

Reference: https://www.youtube.com/watch?v=mLfjzJsN8us
"""

#Code
#Memoization soln
#TC: O(n), SC: O(n), recursive soln
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [-1] * (n + 1)
#         dp[0], dp[1] = 1, 1
#         def climb(k):
#             if dp[k] != -1:
#                 return dp[k]
#             dp[k] = climb(k-1) + climb(k-2)
#             return dp[k]
#         return climb(n)

#Tabulation soln
#TC:O(n), SC:O(n), iterative soln no stack space is used
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         dp = [-1] * (n + 1)
#         dp[0], dp[1] = 1, 1
#        
#         for i in range(2, n+1):
#             dp[i] = dp[i-1] + dp[i-2]   
#         return dp[n]

#Space Optimization soln
#TC:O(n), SC:O(1), the O(n) space is reduce to constant space
class Solution:
    def climbStairs(self, n: int) -> int:
        prev, prev2 = 1, 1
        for i in range(2, n+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        return prev




