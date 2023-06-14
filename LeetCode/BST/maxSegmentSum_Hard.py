"""
Question
https://leetcode.com/contest/biweekly-contest-85/problems/maximum-segment-sum-after-removals/
"""

#Approach
"""
--> This is a simulation problem
--> To get faster insertion and deletion and also to find the max value BST can be used
--> 2 self balancing BST can be used. 1 for keeping track of the segments and the other
for keeping track of the segment sum to find the max amongst them
--> prefix sum can be used for find the subarray sum in O(1) time

Reference: Programming Live with Larry YT 

TC: O(nLog(n)) SC: O(n)
"""

#Code
from sortedcontainers import SortedList
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        N = len(nums)
        INF = 10 ** 20
        prefixSum = [0]
        """
        0 is added at the beggining of prefixSum array because we won't need to handle corner case separately.
        Eg: subarray sum from 0 to i would be prefixSum[i] and for subarray sum betn j and i would be prefixSum[i] - prefixSum[j-1]
        In order to not handle this kind of corner case 0 is added at beggining
        PrefixSum of array [1, 2, 3, 4, 5] would be [0, 1, 3, 6, 10, 15]
        So to find the subarray sum between i and j we would need to add 1 to indices because 0 is added at beggining
        """
        for i in range(N):
            prefixSum.append(prefixSum[-1] + nums[i])
        
        sl = SortedList()
        sums = SortedList()
        total = prefixSum[-1]
        sl.add((0, N-1, total))
        sums.add(total)
        ans = []
        for q in removeQueries:
            #INF is added so that we find the index after q in sl 
            index = sl.bisect_right((q, INF, INF)) - 1
            left, right, total = sl.pop(index)
            sums.discard(total)
            
            if(q != left):
                sl.add((left, q-1, prefixSum[q] - prefixSum[left]))
                sums.add(prefixSum[q] - prefixSum[left])
            if(q != right):
                sl.add((q + 1, right, prefixSum[right + 1] - prefixSum[q + 1]))
                sums.add(prefixSum[right+1] - prefixSum[q+1])
            
            if(len(sums) > 0):
                ans.append(sums[-1])
            else:
                ans.append(0)
        return ans                
            
        