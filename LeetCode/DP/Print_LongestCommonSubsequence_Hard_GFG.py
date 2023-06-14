"""
Question
https://practice.geeksforgeeks.org/problems/print-all-lcs-sequences3413/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-all-lcs-sequences
"""

#Approach
"""
--> Extension of 1143_LCS_Medium.py
--> After finding the LCS we can use the dp table to reconstruct the path
--> Use bottom up approach to create the dp table as top down approaach doesn't necessarily 
fills up the whole table
--> There can be duplicates so use set for that

--> GFG is giving TLE for some test cases, there recommended soln is to brute force
    -https://www.youtube.com/watch?v=gfxdpQIf2NI&t=1014s

--> We are using standard DP path reconstruction and not brute forcing. The idea is from
striver video DP-26: https://www.youtube.com/watch?v=-zI4mrF2Pb4 

TC: O(N1 * N2), SC:O(N1 * N2)
"""

#Code
#Bottom Up Approach
class Solution:
    def all_longest_common_subsequences(self, text1, text2):
        N1, N2 = len(text1), len(text2)

        #Creating the dp table with bottom up approach
        dp = [[-1] * (N2 + 1) for _ in range(N1 + 1)]
        for i in range(N1, -1, -1):
            for j in range(N2, -1, -1):
                if i >= N1 or j >= N2:
                    dp[i][j] = 0                
                elif text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        
        ans = set()
        #print(dp)
        #DP Path reconstruction
        def reconstruct(i, j, path):
            if i == N1 or j == N2:
                currSeq = ''.join(path)
                if currSeq not in ans:
                    ans.add(currSeq)
                return
            if text1[i] == text2[j]:
                path.append(text1[i])
                reconstruct(i+1, j+1, path)
                path.pop()
            elif dp[i + 1][j] > dp[i][j + 1]:
                reconstruct(i + 1, j, path)
            elif dp[i + 1][j] < dp[i][j + 1]:
                reconstruct(i, j + 1, path)
            else:
                reconstruct(i + 1, j, path)
                reconstruct(i, j + 1, path)
        
        
        reconstruct(0, 0, [])
        currAns = list(ans)
        #Arranging in lexicographical order
        currAns.sort()
        return currAns
        
