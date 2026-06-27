# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.head = None 
    
    def addFirst(self , data):
        x = ListNode(data)
        x.next = self.head 
        self.head = x 
    def deleteDuplicates(self, inputhead):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        l = []
        curr = inputhead
        while curr:
            if not l or l[-1] != curr.val:
                l.append(curr.val)
            curr = curr.next

        l = l[::-1]
        for x in l:
            self.addFirst(x)

        return self.head         