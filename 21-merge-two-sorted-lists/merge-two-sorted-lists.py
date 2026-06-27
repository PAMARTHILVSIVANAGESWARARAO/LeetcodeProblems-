# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self):
        self.head = None 
    
    def getList(self):
        curr = self.head
        res = []
        while curr:
            res.append(curr.val)
            curr= curr.next
        return res
    
    def addFirst(self , data , position=0 ):
        self.addAtPosition(position , data)

    def addAtPosition(self, position, new_data):

        x = ListNode(new_data)

        if position == 0:
            x.next = self.head
            self.head = x
            return

        curr = self.head

        for i in range(position - 1):
            if curr is None:
                raise IndexError("Position out of bounds")
            curr = curr.next

        if curr is None:
            raise IndexError("Position out of bounds")

        x.next = curr.next
        curr.next = x


    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]"""
        curr1 = list1
        curr2 = list2

        while curr1:
            self.addFirst(curr1.val)
            curr1 = curr1.next

        while curr2:
            self.addFirst(curr2.val)
            curr2 = curr2.next

        

        res = self.getList()
        res = sorted(res)


        self.head = None

        for value in reversed(res):
            self.addFirst(value)

        return self.head 
        


        