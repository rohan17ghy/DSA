"""
Question
https://leetcode.com/problems/shortest-common-supersequence/description/
"""

#Approach
"""
Approach #1: DP
--> We can have an observation that we need to prepare the -ve satisfaction dishes first (less time) and the
highest satisfaction at last to maximize the like coefficient sum
--> In order to do that we can sort the satisfaction array
--> Now we can apply DP. We need to figure out the subproblem and the recurrence
--> First assume wat the recursive function will return. We asumed the recursive function "Returns the maximum sum
of like-time coefficient between satisfaction[i:] when current time is "time""
--> At each step we need to figure out whether to skip preparing that dish or not
TC: O(N ^ 2), SC: O(N ^ 2)

Approach #2: Greedy
--> For this reference check out "Programming Live with Larry" video
https://www.youtube.com/watch?v=roHueg0p0_Q&t=621s

TC: O(N), SC:O(1)
"""

#Code
#Approach 1: DP
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        N = len(satisfaction)
        satisfaction.sort()
        dp = [[-1] * (N+1) for _ in range(N)]

        #Returns the maximum sum of like-time coefficient between satisfaction[i:] when current time
        #is "time"
        def findMax(i, time):
            if i >= N:
                return 0

            if dp[i][time] != -1:
                return dp[i][time]

            notPreparing = findMax(i+1, time)
            preparing = satisfaction[i] * time + findMax(i+1, time+1)

            dp[i][time] = max(preparing, notPreparing)
            return dp[i][time]
        
        return findMax(0, 1)

#Approach 2: Greedy
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        Greedy soln
        Inspired from Programming Live with Larry 
        https://www.youtube.com/watch?v=roHueg0p0_Q
        """
        """
        [2, 3, 4]
               1 --> 4 (total = 4, best = 4)
            1  2 --> 4 + 4 + 3 = 11(total = 7, best = 11)
         1  2  3 --> 11 + 7 + 2 = 20(total = 9, best = 20)

        """

        N = len(satisfaction)
        satisfaction.sort()

        best = 0
        suffixSum = 0
        for i in range(N-1, -1, -1):
            if best + suffixSum + satisfaction[i] > best:
                best = best + suffixSum + satisfaction[i]
                suffixSum += satisfaction[i]
        return best