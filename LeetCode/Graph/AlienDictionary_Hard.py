"""
Question
https://practice.geeksforgeeks.org/problems/alien-dictionary/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=eventual-safe-states
"""

#Approach
"""
--> Kahn algorithm for topological sort
--> The main thing is to create the adjacency list of the graph of letters
--> After creating the adjacency list rest is topological sort   
"""

#Code
import collections
class Solution:
    def findOrder(self,alien_dict, N, K):
        def compareWords(word1, word2):
            if word1 == word2:
                return None, None
            N1, N2 = len(word1), len(word2) 
            i, j = 0, 0
            while i < N1 and j < N2:
                if word1[i] == word2[j]:
                    i += 1
                    j += 1
                    continue
                return word1[i], word2[j]
            return None, None    
        
          
        adj = collections.defaultdict(set)
        for i in range(1, N):
            u, v = compareWords(alien_dict[i-1], alien_dict[i])
            if u and v:
                adj[ord(u)-ord('a')].add(ord(v)-ord('a'))
                
        incEdges = [0] * K
        for u in adj:
            for v in adj[u]:
                incEdges[v] += 1
        
        q = collections.deque([])
        for letter, count in enumerate(incEdges):
            if count == 0:
                q.append(letter)
                
        ans = []
        while q:
            curr = q.popleft()
            ans.append(chr(curr + ord('a')))
            for v in adj[curr]:
                incEdges[v] -= 1
                if incEdges[v] == 0:
                    q.append(v)
        
        return ans            
        