"""
Question
https://practice.geeksforgeeks.org/problems/merge-two-binary-max-heap0144/1
"""

#Approach:
"""
Merge both arrays and heapify the resultant array
"""
#TC: O(n + m), SC:O(n + m)

#User function Template for python3
import heapq
class Solution():
    def mergeHeaps(self, a, b, n, m):
        #your code here
        c = a + b
        c = list(map(lambda x: -1 * x, c))
        heapq.heapify(c)
        c = list(map(lambda x: -1 * x, c))
        
        return c



