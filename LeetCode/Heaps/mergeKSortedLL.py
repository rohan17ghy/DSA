"""
Question
https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1
"""

#Approach 1: 
"""
--> Keep merging 2 LL's, until 1 final LL is reached

Time Complexity:
TC: O(nk) SC: O(1)
Here n is total number of elements 
"""

#Approach 2:
"""
--> Use a heap to store the first element of the k Linked Lists.
--> Remove the smallest element from the heap
--> Add the next element of the LL to heap, LL which the removed element is part off.

Time Complexity:
TC: O(nlog(k))
SC: O(k)
"""

import heapq
class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        # code here
        # return head of merged list
        
        minHeap = []
        #Count is used to break ties when there are duplicate values of node.data
        count = 0
        for node in arr:
            heapq.heappush(minHeap, (node.data, count, node))
            count += 1
        
        dummy = Node(None)
        prev = dummy
        while(len(minHeap) > 0):
            node = heapq.heappop(minHeap)[2]
            if(node.next != None):
                heapq.heappush(minHeap, (node.next.data, count, node.next))
                count += 1
            prev.next = node
            prev = prev.next
        
        return dummy.next 