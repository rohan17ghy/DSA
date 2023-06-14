# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None

class Solution:

    def createDoublyLinkedList(self, serializedList):

        if(serializedList == None or len(serializedList) == 0):
            print('Linked List is None or empty')
            return None     
        
        head = ListNode(serializedList[0])
        temp = head
        for i in range(1, len(serializedList)):
            temp.next = ListNode(serializedList[i])
            temp.next.prev = temp
            temp = temp.next

        return head       

    def printLL(self, head):
        while(head != None):
            print(head.data, sep=' ')
            head = head.next

    def countTriplets(self, head, x):
        ans = []
        while(head != None):
            triplets = self.countPairs(head.next, x-head.data, head.data)
            ans.extend(triplets)
            head = head.next
        return len(ans)
        
    def countPairs(self, head, target, num1):
        if(head == None):
            return []
        pairs = []
        tail = self.findTail(head)
        
        sum = head.data + tail.data
        while(head.data < tail.data):
            sum = head.data + tail.data
            if(sum == target):
                pairs.append([num1, head.data, tail.data])
                head = head.next
                tail = tail.prev
            elif(sum < target):
                head = head.next
            else:
                tail = tail.prev
        return pairs
        
    def findTail(self, head):
        while(head.next != None):
            head = head.next
        return head



sol = Solution()
list1 = [1, 2, 3, 8, 9]
head = sol.createDoublyLinkedList(list1)
count = sol.countTriplets(head, 13)
print(count)
sol.printLL(head)
