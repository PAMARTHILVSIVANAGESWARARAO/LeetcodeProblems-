# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def __init__(self): self.head = None 

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
        

    def reverse_groups(self, l, k):
        res = []

        for i in range(0, len(l), k):
            group = l[i:i+k]
            if len(group) == k:
                res += group[::-1]
            else:
                res += group

        return res

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        l = []
        curr = head
        while curr:
            l.append(curr.val)
            curr = curr.next
        
        r = self.reverse_groups(l , k)

        for x in reversed(r):
            self.addFirst(x)
        
        return self.head 