"""
The coding style of this problem can be used as a standard template for fixed size sliding window
problems
"""
"""
Q: Minimum swaps required to bring all elements <= K together
"""

def minSwap (arr, n, k) : 
    #Complete the function
    
    #Calc count of numbers <= k
    count = 0
    for num in arr:
        if(num <= k):
            count += 1
    
    #Creating the window of size count
    currWinCount = 0
    for i in range(count):
        if(arr[i] <= k):
            currWinCount += 1
    
    #Initializing the answer
    ans = count-currWinCount
    
    #Moving the window
    for i in range(count, n):
        if(arr[i - count] <= k):
            currWinCount -=1
        if(arr[i] <= k):
            currWinCount += 1
        ans = min(ans, count-currWinCount)
    return ans