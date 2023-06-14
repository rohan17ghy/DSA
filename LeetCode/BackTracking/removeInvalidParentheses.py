"""
Question
https://leetcode.com/problems/remove-invalid-parentheses/
"""
#Approach1: Non-optimized
"""
--> Need to consider all possible combinations
--> At each character, check if including it will make the string balanced(this is done with
the help of stack variable in the remove() argument)
--> At the end of the string check if the currStr created after removing the brackets is balanced
and also if it is achieved by removing minimum brackets
"""
#TC: O(2^N)
#SC: O(N) for stack

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        count = self.numberOfInvalidParen(s)
        hashSet = set()
        self.remove(s, len(s)-count, '', [], hashSet)
        return list(hashSet)
        
    
    def remove(self, s, count, currStr, stack, hashSet):
        if(s == ''):
            if(len(currStr) == count and (not stack)):
                hashSet.add(currStr)
            return
        
        if(s[0].isalpha()):
            self.remove(s[1:], count, currStr + s[0], stack, hashSet)
            return
        
        #2 options, either we consider a parentheses or discard it
        #1st option: we consider s[0]
        if(s[0] == '('):
            stack.append(s[0])
            self.remove(s[1:], count, currStr + s[0], stack, hashSet)
            stack.pop()
        elif(stack and stack[-1] == '('):
            stack.pop()
            self.remove(s[1:], count, currStr + s[0], stack, hashSet)
            stack.append('(')
            
        #2nd option: Don't consider s[0]
        self.remove(s[1:], count, currStr, stack, hashSet)
        
    
    def numberOfInvalidParen(self, s):
        stack = []
        
        for i in range(len(s)):
            if(s[i].isalpha()):
                continue
            
            if(s[i] == '('):
                stack.append(s[i])
            else:
                if(stack and stack[-1] == '('):
                    stack.pop()
                else:
                    stack.append(s[i])
        return len(stack)

#Approach2: Optimized soln
"""
--> In above solution there is scope of optimization
--> We know we can remove only a certian number of brackets, but we are checking that at the end
Problem is that we will create a lot many combinations of brackets if we check at the end. Instead
we can check the number of removals to be made as we make the recursion calls, this will reduce the
number of recursion calls need to be made.
--> We can check whether the string is balanced or not at the end
--> Although this would not reduce the worst case space time complexity but average time complexity
will reduce for many test cases
--> There can be duplicate answers, to handle that we can use map and consider checking for
duplicate ans in a recursion call.   
"""

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        removals = self.numberOfInvalidParen(s)
        ans = []
        self.remove(s, removals, set(), ans)
        return ans
        
    def remove(self, s, removals, hashSet, ans):        
        if(s in hashSet):
            return            
        
        #Optimization for same combination of string appearing multiple times during recursion
        hashSet.add(s)
        
        #Optimization of removing brackets only upto a particular count
        #This is the total removal. Further a bit more optimization can be done by keeping separate
        #track of left bracket removal and right bracket removal
        if(removals == 0):
            if(self.numberOfInvalidParen(s) == 0):
                ans.append(s)
            return
        
        for i in range(len(s)):
            #Removing ith element and recursion call
            self.remove(s[:i] + s[i+1:], removals-1, hashSet, ans)
        
    #Find the number of invalid brackets
    def numberOfInvalidParen(self, s):
        stack = []
        
        for i in range(len(s)):
            if(s[i].isalpha()):
                continue
            
            if(s[i] == '('):
                stack.append(s[i])
            else:
                if(stack and stack[-1] == '('):
                    stack.pop()
                else:
                    stack.append(s[i])
        return len(stack)

#Approach3:
"""
--> One more approach that i have seen is DFS. 
--> Right now not sure how that is done
--> Check out that soln after completing DFS
"""