"""
Question
https://leetcode.com/problems/find-k-closest-elements/
"""

#Approach
"""
--> Use binary search to find the element or it's neighbours if not present in array
--> Instead of doing the search manually we can use bisect.bisect_left()
--> Use two pointers to find the closest elemets from that element

Found some trouble while coding like
--> How to reach to the closest point using Binary search
Ans: This can be done by simple binary search, the thing to observe is
    --> If the element we are searching is present in array than after Binary Search s == e
    --> If the element we are searching is not in array than after Binary search s will be
    at right index of element and e will be at left index of element
                        Before BS: s..................e
                        After BS when not found element:  .......es.......
                        Element was suppose to be between e and s
--> How to handle the cases when e or s is out of the bounds of the array
Ans: If out of bounds then we can directly find the ans
    --> If e < 0 then the ans is first k elements
    --> If s >= N then the ans is last k elements   
"""

#Code
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        s, e = 0, N-1
        orgK = k

        """
        Below while loop can be reduced to 
        s = bisect.bisect_left(arr, x)
        e = s - 1
        """
        while(s <= e):
            mid = (s + e) // 2
            if(arr[mid] < x):
                s = mid + 1
            elif(arr[mid] > x):
                e = mid - 1
            else:
                s = e = mid
                break
        
        if(s == e):
            s += 1
            e -= 1
            k -= 1
        
        #print(s, " ", e)
        while(e >= 0 and s < N and k > 0):
            left_delta = x - arr[e]
            right_delta = arr[s] - x
            
            if(left_delta <= right_delta):
                e -= 1
            else:
                s += 1
            
            k -= 1
        
        #print(s, " ", e)
        if(k > 0):
            if(e < 0):
                return arr[:orgK]
            else:
                return arr[N-orgK:]
        
        return arr[e+1: s]

#Follow up
"""
There is even a better approach when binary search is used but a bit cleverly.
Check out the discussion forum
https://leetcode.com/problems/find-k-closest-elements/discuss/202785/Very-simple-Java-O(n)-solution-using-two-pointers
"""