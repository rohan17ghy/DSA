"""
Question
https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/?envType=daily-question&envId=2023-10-22
"""

#Approach
"""
--> We will start from index == k and then expand the subarray in a greedy fashion 

--> TC: O(N), SC:O(1)
"""

#Code
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        #Greedy solution
        N = len(nums)
        curr_min = nums[k]
        best = nums[k]

        #left and right are not inclusive
        left, right = k-1, k+1

        while left >= 0 or right < N:
            #Most greedy
            #If we can increase the length of subarray without changing the curr_min
            while left >= 0 and nums[left] > curr_min:
                left -= 1
            while right < N and nums[right] > curr_min:
                right += 1

            best = max(best, curr_min * (right - 1 - left))     

            #If nums[left] and nums[right] are both less than nums[k] means that curr_min will change so we will take the higher as per greedy 
            if left >= 0 and right < N:
                if nums[left] > nums[right]:
                    curr_min = nums[left]
                    left -= 1
                else:
                    curr_min = nums[right]
                    right += 1
            elif left >= 0:
                curr_min = nums[left]
                left -= 1
            elif right < N:
                curr_min = nums[right]
                right += 1                    

            #print(left, " ", right)        
            best = max(best, curr_min * (right - 1 - left))     

        return best          
         
           
