class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        res = [0] * (len(arr)) 
        return self.mergeSort(arr, res, 0, n-1)
        
    def mergeSort(self, arr, res, s, e):
        
        mid = (s + e) // 2
        inv_count = 0
        inv_count += self.mergeSort(arr, res, s, mid)
        inv_count += self.mergeSort(arr, res, mid+1, e)
        
        return inv_count + self.merge(arr, res, s, mid+1, e)
        
    
    def merge(self, arr, res, start1, start2, end):
        i = start1
        j = start2
        k = i
        inv_count = 0
        while(i < start2 and j <= end):
            if(arr[i] < arr[j]):
                res[k] = arr[i]
                i += 1
                k += 1
            else:
                res[k] = arr[j]
                j += 1
                k += 1
                inv_count += start2 - i
        
        while(i < start2):
            res[k] = arr[i]
            i += 1
            k += 1
            
        while(j <= end):
            res[k] = arr[j]
            j += 1
            k += 1
        
        return inv_count 

sol = Solution()
arr = [2, 4, 1, 3, 5]
ans = sol.inversionCount(arr, 5)
print(ans)


# list = [1, 2, 3, 4]
# head = sol.createLinkedList(list)
# ans = sol.copyList(head)
# sol.printLL(ans)
