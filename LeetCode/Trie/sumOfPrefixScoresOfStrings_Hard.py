"""
Question
https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
"""

#Approach
"""
Standard Trie Problem

Reference : https://www.youtube.com/watch?v=qQD_CnXGcFM
Programming Live with Larry
"""

#Code
class Node:
    def __init__(self):
        self.edges = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        current = self.root
        for c in word:
            if c not in current.edges:
                current.edges[c] = Node()
            current = current.edges[c]
            current.count += 1

    def find(self, word):
        current = self.root
        t = current.count
        for c in word:
            current = current.edges[c]
            t += current.count
        return t

class Solution:
    def sumPrefixScores(self, words):
        t = Trie()
        for word in words:
            t.add(word)

        c = []
        for word in words:
            c.append(t.find(word))
        return c                                           