class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:

        # dequeue everything from q1 into q2 except last item
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop(0))

        # save last item (top of stack)
        val = self.q1.pop(0)

        # swap q1 and q2 for easier logic - q1 is always the one holding the items
        (self.q1, self.q2) = (self.q2, self.q1)
        return val


    def top(self) -> int:
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop(0))

        val = self.q1[0]

        self.q2.append(self.q1.pop(0))

        (self.q1, self.q2) = (self.q2, self.q1)
        return val


    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()