"""
Question
https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1
"""

#Approach
"""
--> Heapify the given array
--> Take the smallest 2 values from heap
--> Calc the cost from these 2 values
--> Add the sum back to the heap

Time Complexity:
TC: O(nLogn) SC: O(n)
"""
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        heapq.heapify(arr)
        cost = 0
        while(len(arr) > 0):
            num1 = heapq.heappop(arr)
            
            if(len(arr) == 0):
                break
            num2 = heapq.heappop(arr)
            cost += num1 + num2
            heapq.heappush(arr, num1 + num2)
        return cost
