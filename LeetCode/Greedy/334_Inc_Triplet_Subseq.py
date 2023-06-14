"""
Question
https://leetcode.com/problems/increasing-triplet-subsequence/description/
"""

#Approach: 
"""
--> This problem is similar to Longest Increasing Subsequence problem which is a DP problem
--> The Time complexity for that is O(N ^ 2) but it will give TLE for the input given
--> It can be optimized to greedy with O(N) time complexity

TC: O(N); SC: O(1) 
"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        INF = 10 ** 20 
        s1 = INF
        s2 = INF

        for num in nums:
            if num > s2:
                return True
            
            if num > s1:
                s2 = min(s2, num)
            if num < s1:
                s1 = min(s1, num)

        return False            

                    
                
        
        