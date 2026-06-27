# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.head = None 
    
    def addFirst(self , val):
        x = ListNode(val)
        x.next = self.head 
        self.head = x 

    def modifiedList(self, nums, inputhead):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
    
        curr = inputhead

        head = []

        while curr:
            head.append(curr.val)
            curr = curr.next
        
        nums_set = set(nums)
    
    
        result = []
    
        # result = result[::-1]
        for item in head:
            
            if item not in nums_set:
                result.append(item)

        curr = self.head 

        for i in reversed(result):
            self.addFirst(i)
        return self.head 
