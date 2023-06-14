class Solution:
    def threeSumClosest(self, nums, target: int) -> int:   
        nums.sort()
        INF = 10 ** 20
        print(nums)
        def twoSumClosest(nums, i, j, target):
            best = INF
            
            while(i < j):
                current = nums[i] + nums[j]
                print("  ", i, " ", j, " ", best, " ", current, " ", target)
                if(abs(target-current) < abs(target-best)):
                    best = current
                if(current > target):
                    j -= 1
                else:
                    i += 1
            return best
        
        N = len(nums)
        INF = 10 ** 20
        closest = INF
        for k in range(N-2):
            best = twoSumClosest(nums, k + 1, N-1, target-nums[k])
            totalSum = best + nums[k]
            print(totalSum)
            if(abs(target-totalSum) < abs(target-closest)):
                closest = totalSum
        return closest
        
s = Solution()
nums = [4,0,5,-5,3,3,0,-4,-5]
target = -2
ans = s.threeSumClosest(nums, target)
print(ans)