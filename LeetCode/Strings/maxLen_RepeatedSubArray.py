"""
Question
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""

#Approach 1: Offset approach (Brute Force)
"""
--> It is a pattern offset approach
--> Coding it is easy and  it is very intuitive

Eg: 
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

To find the common subarray we can move the array by offset and check for subarray like below
offset = 1
   v  
  [1,2,3,2,1]       
[3,2,1,4,7]
   ^ 

offset = 2
     v  
    [1,2,3,2,1]       
[3,2,1,4,7]
     ^    

offset = 3
       v  
      [1,2,3,2,1]       
[3,2,1,4,7]
       ^ 
offset = 4
         v  
        [1,2,3,2,1]       
[3,2,1,4,7]
         ^

We moved nums1 in the above approach, we also need to 
move the nums2. "[3, 2, 1]" is the longest common subarray and indexof(3) in nums1 > indexof(3) in nums2
So we can't get it moving nums1 right, we need to move it left i.e. we need to move nums2 right as below
offset = 1
   v  
[1,2,3,2,1]       
  [3,2,1,4,7]
   ^ 

offset = 2
     v  
[1,2,3,2,1]       
    [3,2,1,4,7]
     ^    
Above iteration will get the answer

offset = 3
       v  
[1,2,3,2,1]       
      [3,2,1,4,7]
       ^ 
offset = 4
         v  
[1,2,3,2,1]       
        [3,2,1,4,7]
         ^

TC: O(M x N), SC: O(1)
M = len(nums1)
N = len(nums2) 
"""

#Code
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def findL(nums1, nums2):
            N1 = len(nums1)
            N2 = len(nums2)
            
            best = 0
            for offset in range(N2):
                count = 0
                for i in range(N1):
                    if i + offset >= N2:
                        break    
                    if nums1[i] == nums2[i+offset]:
                        count += 1
                        best = max(best, count)
                    else:
                        count = 0
            return best
        
        return max(findL(nums1, nums2), findL(nums2, nums1))


#Appoach2: Binary Search + Hashing(Rabin-Karp)

"""
--> Check out below article for explanation
https://leetcode.com/problems/maximum-length-of-repeated-subarray/discuss/1324248/C%2B%2BPython-DP-KMP-Hashing-Solutions-Clean-and-Concise-O(NlogN)

The hashing algo used in above problem is bit confusing, checkout below tutorial on Rabin Karp hashing 
https://www.youtube.com/watch?v=-WdkLyTeZ3Q&list=PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ&index=202

"""

"""
Rabin-Karp hashing is used.
https://www.youtube.com/watch?v=-WdkLyTeZ3Q&list=PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ&index=202
Can be used as default template for rabin karp
There can still be collisions: For example for the array [2, 2, 2, 2, 2], here for size = 3
index 0-2, 1-3 and 2-4 will have the same hash, but it is expected that for same subarray it will have
same hash.

TC: O((N1 + N2) * Log(min(N1, N2)))
SC: O(M + N)
"""
class Solution:
    def findLength(self, nums1, nums2) -> int:
        for i in range(len(nums1)):
            nums1[i] += 1
        
        for i in range(len(nums2)):
            nums2[i] += 1
        
        def inverse(a, b, m):
            if(b == 0):
                return 1
            if(b % 2 == 0):
                t = inverse(a, b/2, m)
                return (t * t) % m
            else:
                t = inverse(a, (b-1)//2, m)
                t = (t * t) % m
                return (t * a) % m

        mod, base = 10 ** 9 + 7, 103
        N1, N2 = len(nums1), len(nums2)
        power = [1] * max(N1, N2)
        for i in range(1, max(N1, N2)):
            power[i] = power[i-1]*base %mod
            
        hash1, hash2 = [0] * (N1 + 1), [0] * (N2 + 1)
        for i in range(N1):
            hash1[i+1] = (hash1[i] + power[i] * nums1[i] % mod) % mod 
        
        for i in range(N2):
            hash2[i+1] = (hash2[i] + power[i] * nums2[i] % mod) % mod
        
        def getHash(givenHash, left, right):
            Pinv = inverse(power[left], mod-2, mod)
            return (givenHash[right+1] - givenHash[left] + mod % mod) * (Pinv % mod) % mod
        
        def foundSubArray(size):
            seen = defaultdict(list)
            for i in range(N1 - size + 1):
                h = getHash(hash1, i, i + size - 1)
                seen[h].append(i)
            for i in range(N2 - size + 1):
                h = getHash(hash2, i, i + size - 1)
                if h in seen:
                    for j in seen[h]:
                        if nums1[j:j + size] == nums2[i:i + size]:
                            return True
            return False

        left, right, ans = 1, min(N1, N2), 0
        while left <= right:
            mid = (left + right) // 2
            if foundSubArray(mid):
                ans = mid  # Update answer
                left = mid + 1  # Try to expand size
            else:
                right = mid - 1  # Try to shrink size
        return ans

#Approach3: Binary Search + Tuple

"""
--> Same as above algo just that instead of hashing tuples are used
--> To check the equality of two subarrays hashing is used in above algo. Hashing is fine
but the code for it is bit complicated. Instead we can compare the subarrays directly by
creating tuples (better for contests)

TC: O((N1 + N2) * Log(min(N1, N2)))
SC: O(M + N)
"""            

#Code
class Solution:
    # Binary Search Approach
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        
        def ok(k):
            # the idea is to use binary search to find the length `k`
            # then we check if there is any nums1[i : i + k] == nums2[i : i + k]
            s = set(tuple(nums1[i : i + k]) for i in range(N - k + 1))
            return any(tuple(nums2[i : i + k]) in s for i in range(M - k + 1))
        
        # init possible boundary
        l, r = 0, min(N, M)
        while l < r:
            # get the middle one
            # for even number of elements, take the upper one
            m = (l + r + 1) // 2
            if ok(m): 
                # include m
                l = m
            else:
                # exclude m
                r = m - 1
        return l


#Approach 4:

"""
--> There is a more famous DP approach to this question but not the most optimized algo
--> The most optimized approach is Approach2 and Approach3 using Binary Search
""" 
        