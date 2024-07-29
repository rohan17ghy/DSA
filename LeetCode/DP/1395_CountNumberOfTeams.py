"""
Question
https://leetcode.com/problems/count-number-of-teams/description/
"""

#Approach
"""
-> In this DP problem it is easier to approach this problem bottom up compared to top down recursion approach
-> The intuition is that if for an index i, let's consider that the teams ends at index i, from there we can traverse from 0...i and get the pairs
where it meets the condition. Without memoization we need O(n ^ 2) to find the pairs multiplied by O(n) to find triplets, so in total O(n^3).
-> We can memoize the pairs that will reduce the time complexity to O(n ^ 2) 
"""

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)

        #Increment and decrement array ending at inc[i] and dec[i] for 2 elements
        #Ex: inc[i] is the number of elements from 0..i-1 where their rating < rating[i]
        #Ex: dec[i] is the number of elements from 0..i-1 where their rating > rating[i]
        """
        In this DP problem bottom up approach is more intuitive than top down recursion solution
        """
        inc = [0] * N
        dec = [0] * N

        for i in range(1, N):
            for j in range(0, i):
                if rating[j] < rating[i]:
                    inc[i] += 1
                else:
                    dec[i] += 1
        
        teams = 0
        #Calculating teams with the help of inc, dec array
        for i in range(2, N):
            for j in range(0, i):
                if rating[j] < rating[i]:
                    teams += inc[j]
                else:
                    teams += dec[j]

        return teams