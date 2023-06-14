from collections import defaultdict
"""
Here offset logic is one tool to solve this type of questions
Intuition written in hand written notes. Please refer that
"""
"""
Here offset logic is one tool to solve this type of questions
Rabin-Karp. Please refer that
"""
class Solution:
    def findLength(self, nums1, nums2) -> int:        
        #Adding 1 to both nums1 and nums2, because for nums1[i] == 0 or nums2[i] == 0
        #there will be collisions in the hashing
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
                    if(len(seen[h]) > 1):
                        print(seen," ", size)
                        print(hash1, " ", hash2)
                        return False
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

sol = Solution()
nums1 = [0, 0, 0, 0, 0]
nums2 = [0, 0, 0, 0, 0]

print(sol.findLength(nums1, nums2))
            
        
            
            
            
            
                        
                
                    
            
            
            
            
                
        