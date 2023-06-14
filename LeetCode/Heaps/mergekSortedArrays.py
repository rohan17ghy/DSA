"""
Question
https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1
"""

#Approach 1: Brute Force
"""
--> Take 2 arrays and merge them, Repeat this process until 1 array is remaining
"""

#TC: O(k^3) --> Calculate
#SC: O(k^3)

#Approach 2: Using heaps
"""
--> Use minHeap to store the first element of all the k arrays.
--> First element of the minHeap will be the first element in ans
--> After popping from minHeap, get the index for that element
--> Move the index ahead and include that element in the minHeap
"""

#User function Template for python3
import heapq
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        
        minHeap = []
        for i in range(K):
            heapq.heappush(minHeap, (arr[i][0], i, 0))
        
        ans = []
        while(len(minHeap) > 0):
            smallest = heapq.heappop(minHeap)
            i = smallest[1]
            j = smallest[2] + 1
            ans.append(smallest[0])
            if(i < K and j < K):
                heapq.heappush(minHeap, (arr[i][j], i, j))
        
        return ans
