"""
KMP Substring Match

Purpose:
- Implements Knuth-Morris-Pratt (KMP) to check whether `needle` exists in `haystack`.

Approach:
- Build an LPS (Longest Prefix Suffix) array for `needle`.
- Use LPS to avoid re-checking characters after mismatches.

Complexity:
- Time: O(N + M), where N = len(haystack), M = len(needle)
- Space: O(M) for the LPS array

Reference:
- DSA Obsidian notes: "KMP substring match" under Strings.
"""

class Solution:
    def kmp(self, needle: str, haystack: str) -> bool:
        N, M = len(haystack), len(needle)

        def buildLPS(needle: str) -> []:
            N = len(needle)
            lps = [0] * N

            i, j = 1, 0
            while i < N:
                if(needle[i] == needle[j]):
                    lps[i] = lps[i-1] + 1
                    j += 1
                    i += 1                    
                elif(j > 0):
                    j = lps[j-1]                  
                else:
                    lps[i] = 0
                    i += 1 
                
                    
            
            return lps
        
        
        lps = buildLPS(needle)
        i, j = 0, 0
        while(i < N):
            if(needle[j] == haystack[i]):                
                if(j >= M):
                    return True
                i += 1                
                j += 1
            elif(j > 0):
                j = lps[j-1]
            
        return False




                    




