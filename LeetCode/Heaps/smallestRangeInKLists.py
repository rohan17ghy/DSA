"""
Question
https://practice.geeksforgeeks.org/problems/find-smallest-range-containing-elements-from-k-lists/1
"""

#Approach1: Using array to keep track of min and max value

"""
--> Store all the first elements of the array to an array with their row and col index
--> Find the min and max of the array
--> Find the ans
--> Replace the min value with the next value of the array it is part of in the KSortedArray
--> Find the ans and repeat

TC: O(n(k^2)), SC: O(k)
"""

#Code
class Solution:
    def smallestRange(self, KSortedArray, n, k):
        # code here
        # print the smallest range in a new line
        minMaxArr = []
        INF = 10**20
        maxVal = float('-inf')
        for i in range(len(KSortedArray)):
            minMaxArr.append((KSortedArray[i][0], i, 0))
            maxVal = max(maxVal, KSortedArray[i][0])
        
        
        ansLow, ansHigh = 0, INF
        while(True):
            minVal = float('inf')
            minIndex = -1
            #Finding the minimum value from the minMaxArr. TC:O(k)
            for i in range(len(minMaxArr)):
                if(minMaxArr[i][0] < minVal):
                    minVal = minMaxArr[i][0]
                    minIndex = i
                    
            #Updating the answer
            if(maxVal - minVal < ansHigh - ansLow):
                ansHigh = maxVal
                ansLow = minVal
                
            #Removing the smallest value of the array and placing the next value of that array
            r, c = minMaxArr[minIndex][1], minMaxArr[minIndex][2]
            if(r < k and c + 1 < n):
                maxVal = max(maxVal, KSortedArray[r][c+1])
                minMaxArr[minIndex] = (KSortedArray[r][c+1], r, c+1)
            else:
                break
        return [ansLow, ansHigh]

#Approach2: Use minHeap
"""
--> In the previous approach we are using O(k) everytime to find the min value
--> We can use a heap to reduce this time complexity O(log(k))
--> The main concept is to understand that we can keep track of the maxValue of a minHeap
--> Check written notes to understand this concept

TC: O(nklog(k)), SC: O(k)
"""

#Code
import heapq
class Solution:
    def smallestRange(self, KSortedArray, n, k):
        # code here
        # print the smallest range in a new line
        minHeap = []
        INF = 10**20
        maxVal = float('-inf')
        for i in range(len(KSortedArray)):
            heapq.heappush(minHeap, (KSortedArray[i][0], i, 0))
            maxVal = max(maxVal, KSortedArray[i][0])
        
        
        ansLow, ansHigh = 0, INF
        while(True):
            minValTuple = heapq.heappop(minHeap)
            minVal = minValTuple[0]
            
            if(maxVal - minVal < ansHigh - ansLow):
                ansLow, ansHigh = minVal, maxVal
            
            r, c = minValTuple[1], minValTuple[2]
            if(r < k and c + 1 < n):
                heapq.heappush(minHeap, (KSortedArray[r][c + 1], r, c + 1))
                maxVal = max(maxVal, KSortedArray[r][c+1])
            else:
                break
        return [ansLow, ansHigh]

