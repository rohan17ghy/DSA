"""
Question
https://leetcode.com/problems/search-insert-position/description/
"""

#Approach
"""
TEMPLATE FOR BINARY SEARCH
--> We try reducing the window or range at each step
--> Using inclusive bounds for the answer range. Like here ans can be between 0 and N so left = 0
and right = N
--> At the end left = right, and that is the answer or index where ans is supposed to be 

-------------------------------------------------------------------------------
Possibility of Infinite Loop:
    --> It is very easy to get into an infinite loop. Eg: [3, 1]. Here left = 0 = mid( as mid = (left + right) // 2),
    and right = 1.Let say we have the condition such that left = mid then this will cause an infinite loop problem as left
    is already equal to mid so there is no change. Same condition will happen infinitely. To avoid this it is very
    important to keep in mind that for binary search problems it is best to not write a condition where we have to 
    do left = mid

    CONCLUSION: Don't write a condition that will lead to the statement left = mid, always try for left = mid + 1 as
    done in this problem
--------------------------------------------------------------------------------

Reference: https://www.youtube.com/watch?v=804AbLGstq4
"""

#Code
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        #Left and Right inclusive of the answer space
        left = 0
        right = N
    
        #When left == right, we need to break the loop as that is the ans
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left



