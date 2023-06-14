"""
Question
https://leetcode.com/problems/largest-palindromic-number/

--> Concept is easy 
--> Implementation can be tricky
--> practise the coding part
"""

#Approach
"""
--> Use a frequency map and iterate through that to construct the string
--> Remove the leading 0's 
--> Handle the case where num has only 0's

TC: O(n),  SC: O(n)
"""

#Code
"""
Reference 
https://leetcode.com/problems/largest-palindromic-number/discuss/2456655/Python-HashMap-Solution-with-Explanation
"""
class Solution:
    def largestPalindromic(self, num: str) -> str:
        map = collections.Counter(num)
        mid = ''
        even = ''
        for i in '9876543210':
            even += map[i] // 2 * i
            if(not mid and map[i] % 2 != 0):
                mid = i
        even = even.lstrip('0')
        return (even + mid + even[::-1]) or '0'
            
        
                    
            
                
            
        
       
        
        
            
            