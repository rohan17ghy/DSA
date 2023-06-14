"""
Question
https://leetcode.com/problems/stone-game-iii/
"""

#Approach
"""
--> Dynamic Programming with Game thory
--> In Game theory from one player's POV we need to maximize one's score and minimize other's score


"""

#Code
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)
        INF = 10 ** 20
        dp = [INF] * N

        #Return the score for stoneValue[i...N] with turn of Alice or Bob at i
        #+ve means Alice wins, -ve means Bob wins, 0 means a tie
        def playGame(i):
            if i >= N:
                return 0

            if dp[i] != INF:
                return dp[i]

            best = stoneValue[i] - playGame(i+1)
            if i + 1 < N:
                #Maximizing current players score by using max() and minimizing 
                #other players score by substracting playGame()
                best = max(best, stoneValue[i] + stoneValue[i+1] - playGame(i+2))
            if i + 2 < N:
                best = max(best, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - playGame(i+3))
            dp[i] = best
            return dp[i] 

        res = playGame(0)
        print(res)
        if res == 0:
            return "Tie"
        return "Alice" if res > 0 else "Bob"         
