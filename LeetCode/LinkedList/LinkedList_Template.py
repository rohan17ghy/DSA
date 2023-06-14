# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def createLinkedList(self, serializedList, circularIndex = -1):

        if(serializedList == None or len(serializedList) == 0):
            print('Linked List is None or empty')
            return None     
        
        head = ListNode(serializedList[0])
        temp = head
        for i in range(1, len(serializedList)):
            temp.next = ListNode(serializedList[i])
            temp = temp.next

        if(circularIndex != -1):
            index = head
            count = circularIndex
            while(count > 0):
                index = index.next            
                count -= 1
            temp.next = index
        return head       

    def findStartingPointOfLoop(self, head):
        fast = head
        slow = head
        
        while(fast != None):
            fast = fast.next.next
            slow = slow.next
            
            if(slow == fast):
                break
                
        slow = head
        
        while(fast != None):
            fast = fast.next.next
            slow = slow.next
            
            if(slow == fast):
                break
        
        return slow      


sol = Solution()
list = [3, 2, 0, -4]
circularIndex = 1

head = sol.createLinkedList(list, circularIndex)
print(sol.findStartingPointOfLoop(head).val)
