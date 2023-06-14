"""
Question
https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/description/
"""

#Approach
"""
--> Following the binary search template we start with the answer space.
--> For a particular time we need to either go left or right
--> The tricky part is the math to finf the left and right sum    

TC: O(LogN) SC:O(1)
"""

#Code
"""
Reference: https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/solutions/1119801/java-c-python-binary-search/
"""

class Solution:
    def maxValue(self, N: int, index: int, maxSum: int) -> int:
        start = 0
        end = maxSum

        def good(a):
            b = max(a - index, 0)            
            #Sum of sequence from b...a sequence is (a + b) * (a - b + 1) / 2.
            #This can be derived from 1 + 2 + 3....N = N * (N + 1) / 2  
            res = (a + b) * (a - b + 1) / 2
            b = max(a - ((N - 1) - index), 0)
            res += (a + b) * (a - b + 1) / 2

            #For cases where we need to keep on adding 1's
            #Eg: n=4, index=0, maxSum = 4
            #Below code returns 2 but 1 is expected 
            if a <= index:
                res += index - a + 1
            if a <= (N-1) - index:
                res += N-index-a     
            return res - a

        #Since we are using start = mid, it migth lead to TLE so we need to change mid = (start + end + 1) // 2
        #from previous mid = (start + end + 1) // 2
        while start < end:
            mid = (start + end + 1) // 2
            if good(mid) <= maxSum:
                start = mid
            else:
                end = mid - 1

        return start    

