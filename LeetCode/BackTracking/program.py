
class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        # code here
        nums = [0] * n
        finalAns = ''
        def solve(nums, permutation):
            if(len(finalAns) > 0):
                return
            if(k == 0 and len(permutation) == n and len(finalAns) == 0):
                finalAns = ''.join(permutation)
                return 
            
            if(len(permutation) == n):
                k -= 1
                return
            
            for i in range(len(nums)):
                if(nums[i] != 1):
                    permutation.append(i+1)
                    nums[i] = 1
                    solve(nums, permutation)
                    nums[i] = 0
                    permutation.pop()
        
        solve(nums, [])
        return finalAns

sol = Solution()
ans = sol.kthPermutation(4, 3)
print(ans)        