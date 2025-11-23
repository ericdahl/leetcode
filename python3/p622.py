class MyCircularQueue:

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
            self.prev = None

    def __init__(self, k: int):
        self.front = None
        self.rear = None
        self.k = k
        self.len = 0


    def enQueue(self, value: int) -> bool:
        if self.len == self.k:
            return False

        n = ListNode(value)
        n.next = self.front
        n.prev = self.rear
        if self.len == 0:
            self.front = n
        else:
            self.front.prev = n
            self.rear.next = n
        self.rear = n
        self.len += 1


        return True


    def deQueue(self) -> bool:
        if self.len == 0:
            return False

        if self.len == 1:
            self.front = None
            self.rear = None
            self.len = 0
            return True

        new_front = self.front.next
        self.rear.next = new_front
        self.front.prev = self.rear
        self.len -= 1
        self.front = new_front

        return True


    def Front(self) -> int:
        if self.len == 0:
            return -1
        return self.front.val


    def Rear(self) -> int:
        if self.len == 0:
            return -1
        return self.rear.val

    def isEmpty(self) -> bool:
        return self.len == 0


    def isFull(self) -> bool:
        return self.len == self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()