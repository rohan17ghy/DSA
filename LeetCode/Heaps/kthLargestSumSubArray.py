"""
Question
https://practice.geeksforgeeks.org/problems/k-th-largest-sum-contiguous-subarray/1
"""

#Approach
"""
--> Find all subarray sum
--> Use a min heap to find the kth largest element with a heap of size k
"""

from typing import List
import heapq

class Solution:
    def kthLargest(self, N : int, K : int, arr : List[int]) -> int:
        # code here
        minHeap = []
        for i in range(N):
            subSum = 0 
            for j in range(i, N):
                #Here we are calculating the sum for every subarray, instead
                #we can take help of prefix sum which will give some in O(1)
                #SubSum(i, j) = prefixSum[j] - prefixSum[i-1]
                subSum += arr[j]
                if(len(minHeap) < K):
                    heapq.heappush(minHeap, subSum)
                else:
                    if(subSum > minHeap[0]):
                        heapq.heappop(minHeap)
                        heapq.heappush(minHeap, subSum)
        
        return minHeap[0]