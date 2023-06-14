"""
Question
https://leetcode.com/problems/word-ladder-ii
"""

#Approach
"""
--> BFS
--> Continuation to wordladder 1, here the important part is to understand that we need to find all the
paths so our works not done when we reach a node. Also we need to be careful about the time complexity
--> At the very first approach by creating the path at each step and putting in queue would be fine but
that gives TLE in python. 
--> So we can use the below approach of using prev dictionary to store the path information
--> Visited array concept cannot be used as we can reach one node multiple times from different nodes
and we need all the paths. So we use the distance d dictionary    
"""

#Code
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        #Creating the adjacency list
        adj = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hashed_word = word[:i] + "*" + word[i+1:]
                adj[hashed_word].append(word)
        
        #Since we have to find all paths so we can't use a visited array
        #We are using this distance dictionary d 
        d = {}
        #prev is used to store the path, the path can be reconstructed later
        #In my initial approach i tried to put the entire path in the queue and that gave a TLE
        #This prev is a clever approach than that
        prev = collections.defaultdict(list)
        d[beginWord] = 0
        q = collections.deque([])
        q.append(beginWord)

        while q:
            current = q.popleft()
            currentD = d[current]

            for i in range(len(current)):
                hashed_word = current[:i] + "*" + current[i+1:]
                for adjWord in adj[hashed_word]:
                    if adjWord not in d:                        
                        prev[adjWord].append(current)
                        d[adjWord] = currentD + 1
                        q.append(adjWord)
                    #This condition means adjWord is already in d,
                    #that means adjWord is already added to q so no need to repeat that and also no need to change the d                 
                    elif currentD + 1 == d[adjWord]:
                        prev[adjWord].append(current)
                
        ans = []
        #Path reconstruction, used in DP
        def reconstruct(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for prevWord in prev[word]:
                path.append(prevWord)
                reconstruct(prevWord, path)
                path.pop()

        reconstruct(endWord, [endWord])
        return ans 


