class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """

        # CORRECTION 1: Use 'or', not 'and', and return -1.
        if index < 0 or index >= self.size():
            return -1

        curr = self.head
        res = []

        while curr:
            res.append(curr.data)
            curr = curr.next

        return res[index]

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def size(self):
        curr = self.head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        return count

    def addAtTail(self, val, position=None):

        if position is None:
            position = self.size()

        self.addAtIndex(position, val)

    def addAtIndex(self, index, val):

        # CORRECTION 2: If index is invalid, do nothing.
        if index < 0 or index > self.size():
            return

        x = Node(val)

        if index == 0:
            x.next = self.head
            self.head = x
            return

        curr = self.head

        for i in range(index - 1):
            curr = curr.next

        x.next = curr.next
        curr.next = x

    def deleteAtIndex(self, index):

        # CORRECTION 3: Invalid index -> do nothing.
        if index < 0 or index >= self.size():
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head

        for i in range(index - 1):
            curr = curr.next

        # CORRECTION 4: Actually delete the node.
        curr.next = curr.next.next