class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)
        
    def atMost(self, nums, k):
        start = 0
        end = 0
        count = 0
        n = len(nums)
        ans = 0
        while(end < n):
            while(end < n and count <= k):
                if(nums[end] % 2 != 0):
                    count += 1
                    
                if(count <= k):
                    ans += 1
                end += 1
                
            
            while(count > k):
                if(nums[start] % 2 != 0):
                    count -= 1
                
                if(count <= k):
                    ans += 1
                start += 1
        
        while(start < n):
            if(nums[start] % 2 != 0):
                count -= 1
            
            if(count <= k):
                ans += 1
            start += 1
        
        return ans

sol = Solution()
nums = [1, 1, 2, 1, 1]
sol.numberOfSubarrays(nums, 3)