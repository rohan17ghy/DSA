"""
Question
https://leetcode.com/problems/meeting-rooms-iii/
"""

#Approach
"""
--> We use two minHeaps. One to keep track of the meetings ending and the other
to keep track of empty rooms
--> Reference: https://leetcode.com/problems/meeting-rooms-iii/discuss/2527284/Two-Min-Heaps

"""

#Code
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ans = [0] * n
        
        #Create 2 minHeaps. One for keeping track of end of meetings.
        #Other for keeping track of the smallest numbered room which is free for meeting
        calendar = []
        emptyRooms = [i for i in range(n)]
        heapq.heapify(emptyRooms)
        
        for start, end in meetings:
            #Empty the calendar where meeting is already over
            #Free up rooms
            while(calendar and calendar[0][0] <= start):
                heapq.heappush(emptyRooms, heapq.heappop(calendar)[1])
            
            if(len(emptyRooms) > 0):
                firstEmptyRoom = heapq.heappop(emptyRooms)
                ans[firstEmptyRoom] += 1
                heapq.heappush(calendar, (end, firstEmptyRoom, start))
            else:
                lstMeet_end, lstMeet_room, lstMeet_start = heapq.heappop(calendar)
                delay = lstMeet_end - start
                ans[lstMeet_room] += 1
                heapq.heappush(calendar, (end + delay, lstMeet_room, start + delay))
        
        print(ans)
        return ans.index(max(ans))

