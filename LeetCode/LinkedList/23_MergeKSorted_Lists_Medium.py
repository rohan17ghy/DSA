"""
Question
https://leetcode.com/problems/merge-k-sorted-lists/description/
"""

#Approach1
"""
--> Initial approach is that we find lowest among the K lists and add it to the answer
--> Now initially we can use a loop to find the lowest node in O(k) time
TC: O(N*k), SC:O(1)
"""

#Approach 2
"""
--> Instead of using a loop we can use a heap to find the lowest node in O(log(k)) time
TC: O(N * log(K)) SC:O(K)
"""

#Approach1 code
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy
        K = len(lists)
        isNodePre = True
        INF = 10 ** 20

        while isNodePre:
            isNodePre = False
            best = INF
            bestIndex = -1
            for i in range(K):
                if lists[i] is not None:
                    isNodePre = True
                    if lists[i].val < best:
                        best = lists[i].val
                        bestIndex = i
            
            if isNodePre:
                curr = lists[bestIndex]
                lists[bestIndex] = lists[bestIndex].next
                temp.next = curr
                temp = temp.next
                temp.next = None                

        return dummy.next

#Approach2 code
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        K = len(lists)
        heap = []
        for i in range(K):
            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))
        
        dummy = ListNode(-1)
        temp = dummy
        while heap:
            val, i = heapq.heappop(heap)
            curr = lists[i]
            lists[i] = curr.next
            if curr.next is not None:                
                heapq.heappush(heap, (lists[i].val, i))
            temp.next = curr
            temp = temp.next
            temp.next = None    
        
        return dummy.next
        

           




