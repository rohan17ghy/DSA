#User function Template for python3
"""
Question
https://practice.geeksforgeeks.org/problems/partition-array-to-k-subsets/1
"""

#Approach 1: Brute Force, worst soln
"""
--> Create an array of length k where each element signifies a subset
--> Traverse the array and for each element we can consider it to be part of any one of k subset
--> So there can be k options for any element in the array
--> Use a visited array to check which elements are already selected
"""
#TC: O(k^N)
#SC: O(N)

class Solution:
    def isKPartitionPossible(self, a, k):
        #code here
        subSum = self.findSubsetSum(a, k)
        
        #Finding whether a number is whole number 
        if(subSum - int(subSum) != 0):
            return False
        
        if(k > len(a)):
            return False
        
        subsets = [0] * k    
        return self.solve(a, 0, subSum, subsets)    
        
        
    def solve(self, a, index, subSum, subsets):
        if(index >= len(a)):
            return True        
        
        flag = False
        for i in range(len(subsets)):
            if(subsets[i] + a[index] <= subSum):
                subsets[i] += a[index]
                flag = flag or self.solve(a, index + 1, subSum, subsets)
                subsets[i] -= a[index]
        return flag
        
    def findSubsetSum(self, a, k):
        subSum = 0
        for num in a:
            subSum += num
        
        return subSum / k 


#Approach 2: Better soln
"""
--> In the last approach the time complexity is very high. We can reduce this if we take a different
approach
--> The idea is almost same. Instead of selecting an element for any of the k subset, we can create
subset one by one. 
--> So for every element in array we can have 2 options either it will be part of current subset or it 
will be not. So time complexity becomes O(2 ^ N)
--> This is for creating 1 subset, we need to repeat this for k subsets so total time complexity becomes
O(k*(2^N))

--> Note: This algo will not work in leetcode as it is not efficient enough. Check further approach
for optimized solns. This algo works in GFG
"""
#TC: O(k*(2^N)) SC:O(N)

class Solution:
    def isKPartitionPossible(self, a, k):
        #code here
        arrSum = sum(a)
        if(arrSum % k != 0):
            return False
        
        visited = [0] * len(a)
        return self.solve(a, 0, 0, arrSum // k, visited, k)
        
    def solve(self, a, i, currSubSum, subSum, visited, k):
        if(k == 0):
            return True
        
        if(currSubSum == subSum):
            return self.solve(a, 0, 0, subSum, visited, k-1)
        
        flag = False
        for j in range(i, len(a)):
            if(visited[j] != 1 and currSubSum + a[j] <= subSum):
                visited[j] = 1
                flag = flag or self.solve(a, j+1, currSubSum + a[j], subSum, visited, k)
                visited[j] = 0
        return flag

#Approach 3:
#This algo can be optimized by using DP approach and memoization