"""
Question
https://leetcode.com/problems/maximum-number-of-robots-within-budget/
"""

#Approach
"""
--> We can use a variable size sliding window which expands until it exceeds budget
--> The main tricky part of this problem is to find the max over the sliding window
--> We can find the max by using heap. TC: O(nlog(n)) as insertion deletion is O(log(n))
--> A better approach is to use a monoqueue. TC:O(n) as insertion deletion is O(1)
--> PATTERN: Finding max/min over a sliding window can be done with monoqueue
    --> Monoqueue is monotonically increasing or monotonically decreasing queue

TC: O(n) SC:O(n)
"""

#Code
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        #Monoque to find max over the sliding windows
        #Monotonically increasing queue for this question
        
        N = len(runningCosts)
        q = collections.deque([])
        
        i = 0
        maxRobots = 0
        runnCost = 0
        for j in range(N):
            #Expanding the window
            #Adding the jth element to the sliding window, hence updating the monoqueue
            while(q and q[-1][0] < chargeTimes[j]):
                q.pop()
            q.append((chargeTimes[j], j))            
            runnCost += runningCosts[j]           
            
            #Shrinking the window when the current cost exceeds budget            
            while(q and q[0][0] + (j-i+1) * runnCost > budget):
                runnCost -= runningCosts[i]
                i += 1
                #When we shrink the window(increment i) we also need to keep the monoqueue
                #in sync. In sync means we need to remove the elements from the monoqueue
                #which are not part of the window
                if(q and q[0][1] < i):
                    q.popleft()
                         
            maxRobots = max(maxRobots, j-i+1)
        return maxRobots
