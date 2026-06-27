# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __inti__(self):
        self.head = None
    def kthRotate(self , l , k):
        k %= len(l)
        return l[-k:] + l[:-k]

    def addFirst(self , value):
        x = ListNode(value)
        x.next = self.head 
        self.head = x

    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if not head:
            return None

        curr = head 
        l = []
        while curr:
            l.append(curr.val)
            curr=curr.next
        
        l = self.kthRotate(l, k)


        self.head = None

        for x in reversed(l):
            self.addFirst(x)

        return self.head

        