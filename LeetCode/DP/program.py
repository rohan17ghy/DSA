class Solution:
    def specialPerm(self, nums) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums)
        
        #Total permutations when previous element is "prev" with current mask "mask"
        def permutate(prev, mask):
            if mask >= ((1 << N) - 1):
                return 1

            total = 0
            for i in range(N):
                if mask & (1 << i) == 0:
                    if prev % nums[i] == 0 or nums[i] % prev == 0:
                        total += permutate(nums[i], mask | (1 << i)) % MOD
            return total

        return permutate(1, 0)
        


if __name__ == '__main__':
    arr1 = [2, 3, 6]
    sol = Solution()
    print(sol.specialPerm(arr1))