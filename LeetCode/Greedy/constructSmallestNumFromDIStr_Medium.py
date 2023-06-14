"""
Question
https://leetcode.com/problems/construct-smallest-number-from-di-string/
"""

#Approach1: Backtracking or permutations
"""
--> All the permutaions can be found and for each permutation we can check if it 
satisfies the conditions
--> Finding all permutaions can be done in 2 ways
    --> choosing a letter and then backtrack if that is not the correct spot for that number
    --> itertools.permutations(range(1, N+2)), this method can be used to find the 
    permutaions. Check out Larry's soln for more info
    https://www.youtube.com/watch?v=b-vIB0xikOw
"""

#Approach2: Greedy soln
"""
--> We can start with the smallest possible answer - "123456789" (all numbers increasing).
--> If we have decreasing intervals, we reverse the string for those intervals.
--> For example, if the pattern is "IIIDDDID", we will reverse 4567 and 89, and the result
will be 123 7654 98.

IMP: The code is important for this question as it can be noticed that sometimes we need
to change some things so that the coding gets easier and we don't have to handle too many
cases or corner cases
"""

#COde
"""
This can be done by backtracking also
Below is the greedy soln

Below code is of lee
Reference: https://leetcode.com/problems/construct-smallest-number-from-di-string/discuss/2422380/JavaC%2B%2BPython-Easy-Reverse
"""
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        #'I' is added so that coding becomes eaiser and we don't have to handle many
        #corner cases
        pattern += 'I'
        initStr = '123456789'
        stack, ans = [], []
        N = len(pattern)
        for i in range(N):
            #Adding here to the stack works for both when 'I' and 'D'
            stack.append(initStr[i])
            if(pattern[i] == 'I'):
                #Empty the stack when 'I' is encountered
                while(stack):
                    ans.append(stack.pop())
        return ''.join(ans)