class Solution:
    def longestArithSeqLength(self, nums) -> int:
        N = len(nums)
        dp = {}
        #Return the longest arithmetic subsequence from i....N starting with i and 
        #difference "diff" 
        def LAS(i, diff):
            if (i, diff) in dp:
                return dp[(i, diff)]
            
            if i == 7 and diff == 0:
                print('Breakpoint')

            best = 1
            for j in range(i+1, N):                
                if not diff:
                    best = max(best, 1 + LAS(j, nums[j]-nums[i]))
                elif nums[j] - nums[i] == diff:
                    best = max(best, 1 + LAS(j, diff))

            dp[(i, diff)] = best
            
            return best

        for i in range(N):
            LAS(i, None)

        print(dp)
        return max(dp.values())

        


if __name__ == '__main__':
    nums = [24,13,1,100,0,94,3,0,3]
    sol = Solution()
    print(sol.longestArithSeqLength(nums))