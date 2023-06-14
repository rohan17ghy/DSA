"""
Question
https://leetcode.com/problems/kth-missing-positive-number/

--> The naive approach(accepted) is easy but the follow up is medium hence marked as medium
"""

#Approach
"""
--> A very good problem of binary search.
--> Lets understand the approach with respect to this example
Input: arr = [2,3,4,7,11], k = 5
Output: 9
--> Binary search pattern is that we do binary search on the ans space, so in this question the ans
space is the missing numbers. Answers possible will be [6, 7, 8, 9, 10]  i.e. N + 1....k+N
--> The problem now is that we dont know how to do binary search on [6, 7, 8, 9, 10]
this array(cond to go left or right)
--> TOOL: So now instead of using the missing number space we can use the missing numbers index space
The missing number index can be either between 0...N-1 or > N.
--> TOOL: We can find the index of the Kth missing number. Since the number is missing this binary search will
return the index where the missing number could've been found if it was present
--> Now we know the missing number index, from that we can find the missing number as
Case 1: left < N

(left + 1)          +             (k-1)   = left + k
    ^                               ^
missing number                    missing numbers       
at index left                    apart from the kth

Case 2: left = N

       k            -              (arr[N-1] - (N-1+1))     +        arr[N-1]    = k + N = k + left as left = N 
       ^                                     ^
     total                       amount of missing numbers
 missing numbers                      in whole array

--> Time: O(log(n)), Space: O(1)
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        N = len(arr)
        left = 0
        right = N

        #Binary search is finding the index of the missing number 
        #If the missing number is in the array nums range 
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] - (mid + 1) < k:
                left =  mid + 1
            else:
                right = mid

        if left < N:
            return left + k
        else:            
            return k + N  



