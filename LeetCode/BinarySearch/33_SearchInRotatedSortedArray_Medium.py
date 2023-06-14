"""
Question
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""

#Approach
"""
--> The main idea is to understand that when rotating the array, there must be one half of the array that is still in sorted order.
--> Pivot: Here pivot is considered to be the smallest element, from where the sorting disrupts
    Eg: [4, 5, 6, 7, 1, 2, 3]
                     ^
                    Pivot
--> If mid is before the pivot, then from left.....mid the array will be sorted, this info is enough
for binary search, rest can be handled in else condition

Case when nums[left] == nums[mid]:
    --> Since there are no duplicates possible so nums[left] == nums[mid] only when left == mid
    --> left == mid when there are 2 elements. Eg: [3, 4]

Merging the case of nums[left] == nums[mid] with nums[left] < nums[mid]:
    --> The body of else condition of nums[left] == nums[mid] is satisfied by nums[left] < nums[mid], so they are
    merged in the first condition

--> Time: O(log(n)), Space: O(1)
"""

#Code
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        #Pivot is the smallest number
        while(left < right):
            mid = left + (right - left) // 2

            #If mid is before the pivot
            #Equal (=) is there as that condition is merged into this one. Check commented else condition.            
            if nums[left] <= nums[mid]:
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



