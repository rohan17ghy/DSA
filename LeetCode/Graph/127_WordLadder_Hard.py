"""
Question
https://leetcode.com/problems/word-ladder/
"""

#Approach
"""
--> BFS
--> Here the main part is to figure out the adjacency list. After that standard BFS can be applied
--> Problem is how to figure out that "hat" and "hot" are neighbours. h*t can be used to point to both
the words 
"""

#Code
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        #Building the adjacency list
        adjWords = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                adjWords[word[:i] + '*' + word[i+1:]].append(word)
        
        q = collections.deque([])
        q.append((beginWord, 1))    
        hashSet = set(wordList)
        while q:
            word, level = q.popleft()
            hashSet.discard(word)
            print(word, level)
            for i in range(len(word)):
                for adjWord in adjWords[word[:i] + '*' + word[i+1:]]:
                    if adjWord == endWord:
                        return level + 1
                    if adjWord in hashSet:
                        q.append((adjWord, level + 1))                        
        return 0


