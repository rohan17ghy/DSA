"""
Question
https://www.codingninjas.com/codestudio/problems/tug-of-war_985253?leftPanelTab=1
"""

#Approach:
"""
--> Find all possible combination of teams possible
--> For each element of arr we have 2 choices
    1. Either include it in team1
    2. Or include it in team2
--> Need to take care of the condition that team1 and team2 are equally divided
--> We can check this condition at the end of recursion, and if it meets then we can consider that
as a possible answer. But that can include many unnecessary recusrion calls. To reduce these
recursion calls we can take care of teamACount and teamBCount during every recursion
"""

def tugOfWar(arr, n):  
    #this is a shorthand of 
    # countTeamA = n // 2 if n % 2 == 0 else (n + 1) // 2  
    countTeamA = (n + n % 2) // 2
    return solve(arr, 0, 0, 0, countTeamA, n-countTeamA)

def solve(arr, i, teamA, teamB, countTeamA, countTeamB):
    if(i >= len(arr)):
        return abs(teamA-teamB)
    
    ans1 = ans2 = float('inf')
    if(countTeamA > 0):
        ans1 = solve(arr, i+1, teamA+arr[i], teamB, countTeamA-1, countTeamB) 
    if(countTeamB > 0):
        ans2 = solve(arr, i+1, teamA, teamB+arr[i], countTeamA, countTeamB-1)
    return min(ans1, ans2)