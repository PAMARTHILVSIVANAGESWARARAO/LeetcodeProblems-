# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

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

    def addFirst(self , data , position=0 ):
        self.addAtPosition(position , data)

    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        l = []

        for head in lists:
            curr = head
            while curr:
                l.append(curr.val)
                curr = curr.next

        l = reversed(sorted(l))

        self.head = None
        for x in l:
            self.addFirst(x)
        return self.head 
        