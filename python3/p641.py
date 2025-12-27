

class MyCircularDeque:

    class ListNode:
        def __init__(self, val=0, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, k: int):
        self.k = k
        self.head = None
        self.size = 0


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = ListNode(value)
            self.head.next = self.head
            self.head.prev = self.head
            self.size += 1
            return True

        rear = self.head.prev

        old_head = self.head
        head = ListNode(value, old_head)
        head.prev = rear
        old_head.prev = head
        rear.next = head
        self.head = head
        self.size += 1
        return True


    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = ListNode(value)
            self.head.next = self.head
            self.head.prev = self.head
            self.size += 1
            return True

        old_last = self.head.prev

        n = ListNode(value)
        n.prev = old_last
        n.next = self.head
        old_last.next.prev = n
        old_last.next = n
        self.size += 1
        return True


    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        if self.size == 1:
            self.head = None
            self.size -= 1
            return True

        old_last = self.head.prev
        old_second = self.head.next

        old_last.next = old_second
        old_second.prev = old_last
        self.head = old_second
        self.size -= 1
        return True


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self.size == 1:
            self.head = None
            self.size -= 1
            return True

        old_second_last = self.head.prev.prev
        old_head = self.head

        old_second_last.next = old_head
        old_head.prev = old_second_last
        self.size -= 1

        return True


    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.prev.val


    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()