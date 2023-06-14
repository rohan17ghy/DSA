"""
Question
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""

#Approach
"""
Prerequisite: 33_SearchInRotatedSortedArray_Medium.py

--> The approach is exactly same as the prerequisite
--> Because of duplicates there is one additional case when nums[left] == nums[mid] == nums[right]
where left != mid != right.
--> Eg: [3, 4, 5, 6, 3, 3, 3, 3, 3], [3, 3, 3, 3, 4, 5, 6, 3]. 
--> Here we are not sure where the pivot is or where to find the target. So we reduce the window from 
both sides. We are not loosing any ans as nums[mid] is still in window if that is the ans

Time: O(log(n)), Space: O(1)
"""

#Code
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        #Pivot is the smallest number
        while(left < right):
            mid = left + (right - left) // 2

            if nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
            #If mid is before the pivot
            #Equal (=) is there as that condition is merged into this one. Check commented else condition.            
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            #If mid is after the pivot
            elif nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            #Condition when nums[mid] == nums[left]
            #Since there are no duplicates nums[mid] == nums[left] only when left == mid
            #Below lines are commented as the body is satisfied by the if condition so it is merged with that
            # else:
            #     if target == nums[mid]:
            #         right = mid
            #     else:
            #         left = mid + 1

        
        if nums[left] == target:
            return left
        return -1



