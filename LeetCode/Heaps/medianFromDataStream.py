"""
Question
https://leetcode.com/problems/find-median-from-data-stream/
"""

#Approach1: BruteForce using sorting
"""
--> Fetch the number from stream and store in array
--> After fetching every num we can sort the array and find the median

TC: O((n^2)log(n))
SC: O(n)
"""

#Approach2: Using 2 heaps
"""
--> We need to fetch the middle two elements after every fetch from the stream
--> We can divide the incoming values into 2 heaps such that 1st half goes to a maxHeap
and second half goes to a minHeap.
--> Median would be average of top of the heap of both minHeap and maxHeap
--> In case there are odd numbers we will store the num in the right Heap (minHeap) 
"""

#Code
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        #If length are equal, that means even numbers are there and after adding it would
        #be odd and we would add it to the right heap(minHeap). Now we need to place this
        #number appropriately either in left or right heap.
        #Since we know that ultimately we have to push to right heap. So we can first do
        #a heappushpop() to the left heap to find the highest num in maxHeap and then
        #push that num in the right heap. This would ensure median are at top of both the
        #heaps
        if(len(self.minHeap) == len(self.maxHeap)):
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))
        #else condition will only mean that len(minHeap) > len(maxHeap)
        #Similar to the above logic we would add to the left heap to make the size equal
        #So we would do a heappushpop() first to the right heap and then push the smallest
        #value of right heap to the left heap. This would ensure the meadian are at
        #top of heap
        else:
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))
    
        
        

    def findMedian(self) -> float:
        if(len(self.maxHeap) == len(self.minHeap)):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            return self.minHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
