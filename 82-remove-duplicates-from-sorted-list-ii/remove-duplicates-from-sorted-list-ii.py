# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self):
        self.head = None 
    
    def addFirst(self,data):
        x = ListNode(data)
        x.next = self.head 
        self.head = x 

    def deleteDuplicates(self, input_head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """ 

        s = []

        curr = input_head
        while curr:

            
            s.append(curr.val)
            curr = curr.next 
        
        curr = self.head 

       

        l = []
        
        
        i = 0
        while i < len(s):

            if i == len(s) - 1 or s[i] != s[i + 1]:
                l.append(s[i])
                i += 1
            else:
                while i < len(s) - 1 and s[i] == s[i + 1]:
                    i += 1
                i += 1


        

        for x in reversed(l):
            self.addFirst(x)
        return self.head 


        