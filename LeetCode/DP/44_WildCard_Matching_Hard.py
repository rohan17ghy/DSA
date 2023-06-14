"""
Question
https://leetcode.com/problems/wildcard-matching/description/
"""

#Approach
"""
--> The main idea is to figure out the subproblem and the recurrence
--> Write down wat the recursive fn should return 
--> The base case can be little tricky which can give wrong answer

TC: O(N * M), SC: O(N * M)
"""

#Code
#Top Down Approach
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        N, M = len(s), len(p)
        has_cache = [[False] * (M+1) for _ in range(N+1)]
        cache = [[False] * (M+1) for _ in range(N+1)]

        #Returns whether s[i1:] is matched by p[i2:]
        def isWildCardMatch(i1, i2):
            if i1 == N and i2 == M:
                return True
            if i2 == M:
                return False
            #Tricky Edge case 
            #When s string is over but p string is not over and having only "*" which can match
            #Eg: s="", p="*********"
            if i1 == N: 
                if p[i2] == "*":                
                    cache[i1][i2] = isWildCardMatch(i1, i2 + 1)
                    has_cache[i1][i2] = True
                    return cache[i1][i2]
                else:
                    cache[i1][i2] = False
                    has_cache[i1][i2] = True
                    return cache[i1][i2]
            
            
            if has_cache[i1][i2]:
                return cache[i1][i2]

            if s[i1] == p[i2]:
                cache[i1][i2] = isWildCardMatch(i1+1, i2+1)
                has_cache[i1][i2] = True
                return cache[i1][i2]
            else:
                if p[i2] == "?":
                    cache[i1][i2] = isWildCardMatch(i1 + 1, i2 + 1)
                    has_cache[i1][i2] = True
                    return cache[i1][i2]
                if p[i2] == "*":
                    ans = isWildCardMatch(i1 + 1, i2) or isWildCardMatch(i1 + 1, i2 + 1) or isWildCardMatch(i1, i2 + 1)
                    cache[i1][i2] = ans
                    has_cache[i1][i2] = True
                    return cache[i1][i2]
                
                cache[i1][i2] = False
                has_cache[i1][i2] = True
                return cache[i1][i2]
        
        return isWildCardMatch(0, 0)
