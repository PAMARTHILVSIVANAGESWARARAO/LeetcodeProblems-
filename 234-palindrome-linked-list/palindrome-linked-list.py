# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        l = []
        curr = head 

        while curr:
            l.append(curr.val)
            curr = curr.next
        
        res = l == l[::-1]
        return res 
        