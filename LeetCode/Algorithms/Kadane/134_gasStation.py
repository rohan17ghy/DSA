"""
Question
https://leetcode.com/problems/gas-station/description/
"""

#Approach
"""
--> Approach is similar to kadane algo to find the max subarray sum
--> Here instead of finding the max subarray sum we have to find the starting index such that we can travel
through the entire array.
--> If the current gas is -ve than we can't continue and we have to start from next index.
--> Travelling through the array 2 times is enough to find the start index and travel through the entire array
in circular fashion 

"""

#TC: O(N)  SC:O(N), Space complexity is because we are doubling the input cost and gas
#We can do even without doubling the arrays. Check next solution
#Code
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        gas = gas + gas
        cost = cost + cost

        start = 0
        current = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            current += g
            current -= c

            if current < 0:
                start = i+1
                current = 0

            if i - start + 1 >= N:
                return start
        return -1

#Solution 2 without doubling the array
#Code
#TC: O(N)  SC: O(1)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        start = 0
        current = 0
        for i in range(2*N):
            g = gas[i%N]
            c = cost[i%N]
            current += g
            current -= c

            if current < 0:
                start = i+1
                current = 0

            if i - start + 1 >= N:
                return start
        return -1