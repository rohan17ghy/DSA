"""
Question
https://leetcode.com/problems/minimum-falling-path-sum/description/
"""

#Approach
"""
--> GFG platform giving TLE, In coding ninjas it works
--> concept of take and notTake

TC: O(N * total), SC:O(N * total)
"""

#Code
from os import *
from sys import *
from collections import *
from math import *

from typing import List


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    # write your code here
    # Code here
    # Code here
    total = sum(arr)
    mod = 10 ** 9 + 7
    dp = [[-1] * (total+1) for _ in range(n)]
    def count(i, s1Sum):
        if s1Sum > (total + d) / 2:
            return 0
        if i == n:
            if s1Sum == (total + d) / 2 and s1Sum >= total / 2:
                #print(currAns, " ", i, " ", s1Sum)
                return 1
            return 0
            
        if dp[i][s1Sum] != -1:
            return dp[i][s1Sum]
        
        take = count(i+1, s1Sum + arr[i])
        notTake =  count(i+1, s1Sum)
        dp[i][s1Sum] = (take + notTake) % mod
        #print(currAns, " ", i, " ", s1Sum)
        #print(i, " ", s1Sum, " ", dp[i][s1Sum])
        return dp[i][s1Sum]
    ans = count(0, 0)
    return ans


        

           




