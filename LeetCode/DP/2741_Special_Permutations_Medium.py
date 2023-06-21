"""
Question
https://leetcode.com/problems/special-permutations/description/
"""

#Approach
"""
--> The main learning from this problem is that certain problem we need to brute force and there
can't be a better solution
--> We can improve the time complexity with DP but it is still a brute force solution and 
nothing clever.

"""

#Code
class Solution:
    def specialPerm(self, nums) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums)
        
        #Total permutations when previous element is "prev" with current mask "mask"
        @cache
        def permutate(prevInd, mask):
            if mask >= ((1 << N) - 1):
                return 1

            prev = nums[prevInd] if prevInd >= 0 else 1
            total = 0
            for i in range(N):
                if mask & (1 << i) == 0:
                    if prev % nums[i] == 0 or nums[i] % prev == 0:
                        total = (total + permutate(i, mask | (1 << i))) % MOD
            return total

        return permutate(-1, 0)

