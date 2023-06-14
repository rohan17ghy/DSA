def minSwap (arr, n, k) : 
    #Complete the function
    
    #Count the number of elements <= k
    count = 0
    for i in range(n):
        if(arr[i] <= k):
            count += 1
    
    #Creating the windows
    start = 0
    end = 0
    
    ans = n
    currCount = 0
    while(end < n):
        while(end - start < count):
            if(arr[end] <= k):
                currCount += 1
            end += 1
        
        #Calculate the answer
        ans = min(ans, count - currCount)

        #Adjusting the currCount value in the updated window
        if(arr[start] <= k):
            currCount -= 1
            
        if(end < n and arr[end] <= k):
            currCount += 1
        
        #Move the pointers ahead
        start += 1
        end += 1

        #Calculate the answer
        ans = min(ans, count - currCount)
    
    return ans

def convertStringToArray(str):
    return list(map(lambda num : int(num), str.split(' ')))


arr = convertStringToArray("19 9")
print(minSwap(arr, 2, 18))
# sol.levelOrderTraversal(root)