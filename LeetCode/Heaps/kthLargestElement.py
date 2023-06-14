"""
https://practice.geeksforgeeks.org/problems/k-largest-elements4206/1
"""

#Approach1: Sorting
"""
--> Sort the elements of the array
--> Return the array k element from the end(i.e. arr[-k:])
"""
#Tc: O(nlog(n)), SC: O(1)

#Approach2: Heaps
"""
--> Create a min heap from the first k elements of array
--> from k to n elements check if the element is greater than the smallest element in heap, then replace 
--> At the end the heap will have the k largest elements
--> Please note that instead of taking k elements in heap we can create a heap out of the entire array but that will
have worse time complexity than heap with k elements
"""
#TC: O(nlog(k)), SC: O(k)

import heapq
class Solution:

	def kLargest(self,arr, n, k):
		# code here
		minHeap = arr[:k]
		heapq.heapify(minHeap)
		for i in range(k, n):
			if(arr[i] > minHeap[0]):
				heapq.heappop(minHeap)
				heapq.heappush(minHeap, arr[i])
		
		ans = []
		while(len(minHeap) > 0):
			ans.append(heapq.heappop(minHeap))
		
		self.reverse(ans)
		return ans
	
	def reverse(self, arr):
		i = 0
		j = len(arr)-1
		
		while(i < j):
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
			i += 1
			j -= 1