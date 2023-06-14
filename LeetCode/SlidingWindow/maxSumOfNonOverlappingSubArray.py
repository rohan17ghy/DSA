#Approach1: PrefixSum
#TC: O(n) SC:O(n)
class Solution1:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        return max(self.maxSum(nums, firstLen, secondLen), self.maxSum(nums, secondLen, firstLen))
            
        
    def maxSum(self, nums, firstLen, secondLen):
        n = len(nums)
        
        #Creating the prefixSum from the first array
        prefixSum = [-1] * len(nums)
        
        subSum = 0
        for i in range(firstLen):
            subSum += nums[i]
        
        prefixSum[firstLen-1] = subSum
        
        for i in range(firstLen, len(nums)):
            subSum += nums[i]
            subSum -= nums[i-firstLen]
            prefixSum[i] = max(prefixSum[i-1], subSum)
            
        
        start = n - secondLen - 1
        winSum = 0
        
        #Creating the window
        for i in range(start + 1, n):
            winSum += nums[i]
        
        #Calculating ans for first window
        ans = winSum + prefixSum[start]
        
        #Moving the window
        for i in range(start, 0, -1):
            winSum += nums[i]
            winSum -= nums[i + secondLen]
            
            ans = max(ans, winSum + prefixSum[i-1])
        return ans


#Approach2: 
#TC: O(n) SC: O(1)
class Solution1:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        return max(self.maxSum(nums, firstLen, secondLen), self.maxSum(nums, secondLen, firstLen))
            
        
    def maxSum(self, nums, firstLen, secondLen):
        n = len(nums)
        
        #Creating the prefixSum from the first array
        prefixSum = [-1] * len(nums)
        
        subSum = 0
        for i in range(firstLen):
            subSum += nums[i]
        
        prefixSum[firstLen-1] = subSum
        
        for i in range(firstLen, len(nums)):
            subSum += nums[i]
            subSum -= nums[i-firstLen]
            prefixSum[i] = max(prefixSum[i-1], subSum)
            
        
        start = n - secondLen - 1
        winSum = 0
        
        #Creating the window
        for i in range(start + 1, n):
            winSum += nums[i]
        
        #Calculating ans for first window
        ans = winSum + prefixSum[start]
        
        #Moving the window
        for i in range(start, 0, -1):
            winSum += nums[i]
            winSum -= nums[i + secondLen]
            
            ans = max(ans, winSum + prefixSum[i-1])
        return ans

