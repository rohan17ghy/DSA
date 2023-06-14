"""
Question
https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1
"""
#Approach
"""
--> Create a frequency map of the characters
--> Find all the possible permutations. We have two cases while traversing through frequency map
    1. Either we consider the character
    2. or we don't consider the character and move ahead
--> At the end of recursion, store the permutation in an array
"""
#TC: O(n! * n),  SC: O(n)

class Solution:
    def find_permutation(self, S):
        # Code here
        #Frequency map of alphabets
        alpha_fre = [0] * 26
        ordA = ord('A') if S.isupper() else ord('a')
        for char in S:
            alpha_fre[ord(char)-ordA] += 1 
        ans = []
        permutation = []
        
        self.solve(len(S), ordA, alpha_fre, permutation, ans)
        
        return ans
        
    def solve(self, n, ordA, alpha_fre, permutation, ans):
        if(len(permutation) == n):
            ans.append(''.join(permutation))
            return
        
        for i in range(len(alpha_fre)):
            if(alpha_fre[i] != 0):
                #Plan is to first consider the character, then avoid that character
                #Considering the character
                permutation.append(chr(i+ordA))
                alpha_fre[i] -= 1
                self.solve(n, ordA, alpha_fre, permutation, ans)
                alpha_fre[i] += 1
                permutation.pop()
                
                #For avoiding the character we don't need to do anything
                #Simply move to next element in alpha_fre which the loop
                #automatically does