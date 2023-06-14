"""
Question
https://leetcode.com/contest/biweekly-contest-85/problems/maximum-segment-sum-after-removals/
"""

#Approach: 
"""
Writing the approach os some problems are very difficult, difficult to note down. This is one of those problems
Please check the reference article for the approach
"""


"""
Reference: https://leetcode.com/problems/minimum-replacements-to-sort-the-array/discuss/2388143/Python-Google-interview-problem-why-strategy-beats-implementation

"""
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N = len(nums)
        prev = nums[N-1]       
        splits = 0
        for i in range(N-2, -1, -1):
            if(nums[i] > prev):
                #k = Number of numbers created after the break
                #If nums[i] was exactly divisble by prev it would have been nums[i] / prev
                #If nums[i] is not exactly divisble then we take one more number 
                #Above logic is ceil(nums[i] / prev)
                #Formula --> ceil(a/b) = (a +  b - 1) // b
                k = (nums[i] + prev - 1) // prev
                
                #For generating k nums from 1 number k-1 split needs to be done
                splits += k-1
                
                #Need to find the next prev before moving to next iteration
                #prev will be the first num in the splitted numbers
                #First num will be floor(nums[i] / k)
                prev = nums[i] // k
            else:
                prev = nums[i]
        return splits
                    
                
        
        