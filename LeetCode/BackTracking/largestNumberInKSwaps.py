"""
Question
https://practice.geeksforgeeks.org/problems/largest-number-in-k-swaps-1587115620/1
"""

#Approach
"""
--> To make a number higher we need to swap arr[i] and arr[j] such that
    1. arr[j] is higher that arr[i]
    2. j > i
--> For every index we find the max successor of that number on right
--> There can be multiple instances of max sucessor on the right. Try the combinations of swapping 
with every max successor on right.Eg: [1, 2, 3, 5, 6, 5, 6, 6] Max Successor of 3 are 6 at index 4, 6, 7
--> We might be thinking why do we need to explore the combinations by swapping with every max successor
on right rather do it with the last max successor. This approach looks fine but it will fail for some
test cases
--> Similarly only swapping with first max successor is also not right as some of the test cases might
fail
--> For detailed explanation with examples see notes
"""

class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        #code here
        ans = list(s)
        self.solve(list(s), k, 0, ans)
        return ''.join(ans)
    
    def solve(self, arr, k, index, ans):
        if(k == 0 or index >= len(arr)):
            return
        
        #Finding the maximum successor
        maxSuc = self.findMaxSuc(arr, index)
        
        #If no successor higher than arr[index], then move to next index
        #No swaps possible for index
        if(maxSuc == arr[index]):
            self.solve(arr, k, index+1, ans)
            return
        
        for i in range(index+1, len(arr)):
            if(arr[i] == maxSuc):
                self.swap(arr, index, i)
                self.UpdateMaxArray(ans, arr)
                self.solve(arr, k-1, index + 1, ans)
                self.swap(arr, index, i)
            
        
    def findMaxSuc(self, arr, index):
        ans = arr[index]
        for i in range(index+1, len(arr)):
            if(arr[i] > ans):
                ans = arr[i]
        return ans
        
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    #UPdating the values of ans array
    def UpdateMaxArray(self, ans, arr2):
        for i in range(len(ans)):
            if(ans[i] > arr2[i]):
                return
            if(ans[i] < arr2[i]):
                break
            
        for i in range(len(ans)):
            ans[i] = arr2[i]
        