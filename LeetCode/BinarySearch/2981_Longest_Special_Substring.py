"""
Question
https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i
"""

#Approach
"""
PATTERN: Binary Search on answer  


TC: O(NLogN)
SC: O(N) 
"""

#Code
class Solution:
    def maximumLength(self, s: str) -> int:
        N = len(s)
        start, end = 0, N-2

        def isGood(max_count):
            ctr = collections.Counter()
            ans = collections.Counter()
            for i in range(N):
                ctr[s[i]] += 1

                if i >= max_count:
                    if ctr[s[i-max_count]] == 1:
                        del ctr[s[i-max_count]]
                    else:
                        ctr[s[i-max_count]] -= 1

                if i >= max_count-1:
                    if len(ctr) == 1:
                        ans[next(iter(ctr))] += 1
                        
            for key, val in ans.items():
                if val >= 3:
                    return True
            return False

        while start < end:
            mid = (start + end + 1) // 2
            if isGood(mid):
                start = mid
            else:
                end = mid - 1 
        
        
        return start if start > 0 else -1
        