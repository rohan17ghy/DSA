#binarySearch #tle #template #pattern 

![[ExcalidrawEmbeds/BinarySearch/Ex-Binary_Search | 1000]]


# Complete Code

```python fold title:findMin.py
class Solution:

    def findMin(self, nums: List[int]) -> int:

        N = len(nums)
        start, end = 0, N-1  

        while start < end:
            mid = start + (end - start) // 2
            
            #Edge case: when start, end and mid are not unique indices.
            #when mid is calculated to be equal to start
            #possible only when end = start + 1.
            #this is done to avoid TLE    
            if end == start + 1:
                if nums[end] < nums[start]:
                    start = end
                else:
                    end = start
            #2 cases are possible
            #if mid is towards the left of min value
            elif nums[mid] > nums[start] and nums[mid] > nums[end]:
                start = mid
            #If mid is towards the right of min value
            else:
                end = mid
                
        return nums[start]
```