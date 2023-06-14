"""
Question
https://leetcode.com/problems/fruit-into-baskets/description/
"""

#Approach
"""
--> We can use a variable size sliding window which expands, we also reduce the size of the window if there
are more than 2 different types of fruits in the window
--> To find whether there are more than 2 different fruits we can use a dictionary and keep adding and deleting 
elements.
TC: O(n) SC:O(1)
"""

#Code
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)

        i = 0
        counter = collections.Counter()
        ans = 0
        for j in range(N):
            counter[fruits[j]] += 1
            while len(counter) > 2:
                print(counter)
                counter[fruits[i]] -= 1
                if counter[fruits[i]] == 0:
                    del counter[fruits[i]]
                i += 1
            ans = max(ans, j-i+1)
        
        return ans
