class MyLinkedList:

    class LinkedNode:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None

    def _getNodeAtIndex(self, index:int) -> LinkedNode:
        c = self.head
        if not c:
            return None

        for i in range(index):
            if not c:
                return None
            c = c.next
        return c

    def _length(self) -> int:
        c = self.head
        length = 0
        while c:
            c = c.next
            length += 1
        return length

    def get(self, index: int) -> int:
        n = self._getNodeAtIndex(index)
        if not n:
            return -1
        return n.val


    def addAtHead(self, val: int) -> None:
        self.head = self.LinkedNode(val, self.head)


    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = self.LinkedNode(val)
            return

        c = self.head
        while c and c.next:
            c = c.next
        c.next = self.LinkedNode(val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        length = self._length()
        if index > length:
            return

        if index == length:
            self.addAtTail(val)
            return

        before = self._getNodeAtIndex(index - 1)
        before.next = self.LinkedNode(val, before.next)



    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._length():
            return

        if index == 0:
            self.head = self.head.next
            return

        before = self._getNodeAtIndex(index - 1)
        before.next = before.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)