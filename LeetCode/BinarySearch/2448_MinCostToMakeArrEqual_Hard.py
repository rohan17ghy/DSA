"""
Question
https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/
"""

#Approach
"""
PATTERN: TERNARY SEARCH
--> Check out this video for reference https://www.youtube.com/watch?v=dI8L9o1j77c
--> In the below code we can observe that there is a possibility of infinite loop when
we are doing start = mid1 or end = mid2. To avoid this we are moving to the next element when
we encounter this situation. This is a nice trick to avoid infinite loops in Binary Search's.
There are more tricks to avoid infinite loops, check out index.txt for other tricks     


TC: O(NLogN) 
"""

#Code
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        start, end = min(nums), max(nums)

        #Function which calc the cost if all the number in nums is changed to x
        def f(x):
            totalCost = 0
            for i, num in enumerate(nums):
                totalCost += abs(x - num) * cost[i]
            return totalCost    

        while start < end:
            mid1, mid2 = start + (end - start) // 3, end - (end - start) // 3
            if f(mid1) < f(mid2):
                #This if else is done to avoid infinite loop when end = mid2 is done
                if end == mid2:
                    end = mid2 - 1
                else:     
                    end = mid2
            else:
                #This if else is done to avoid infinite loop when start = mid1 is done
                if start == mid1:
                    start = mid1 + 1
                else:
                    start = mid1

        return f(start)

