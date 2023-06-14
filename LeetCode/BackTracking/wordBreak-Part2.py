"""
Question
https://practice.geeksforgeeks.org/problems/word-break-part-23249/1
"""
#Approach
"""
--> Break the word in all possible combinations
--> If the words are part of dictionary then store in ans
"""
#TC: O(N^2 * n) --> where N = length of word, n = number of words in dict
#SC: O(N^2) --> not sure but i think mostly because of the substrings created and passed
#to another recursive function call. Please confirm this understanding ????


class Solution:
    def wordBreak(self, n, dict, s):
        # code here
        ans = []
        self.wordBreakHelper(s, dict, [], ans)
        return ans
        
    def wordBreakHelper(self, s, dict, sentence, ans):
        if(s == ''):
            ans.append(' '.join(sentence))
            return
        
        for i in range(len(s)):
            if(s[:i+1] in dict):
                sentence.append(s[:i+1])
                self.wordBreakHelper(s[i+1:], dict, sentence, ans)
                sentence.pop()