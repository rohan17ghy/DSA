#User function Template for python3
#Implemented using two stacks. O(n) | O(n)
#GFG soln seems complicated in 1st look

class Solution:
    
    #Function to evaluate a postfix expression.
    def redundantBrackets(self, s):
        stack = []
        booleanStack = []
        #operatorPresent = False

        for char in s:
            if(char == '('):
                stack.append(char)
                booleanStack.append(False)
                #operatorPresent = False
            elif(char == ')'):
                # if(operatorPresent == False):
                #     return True    
                # operatorPresent = False
                if(booleanStack[-1] == False):
                    return True
                stack.pop()
                booleanStack.pop()
            elif(not char.isalpha()):
                booleanStack.pop()
                booleanStack.append(True)
        
        return False                    

        
        
sol = Solution()
res = sol.redundantBrackets("((a+b)*(c+d))")
print(res)