class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_value = deque() # "parallel stack" containing min value so far

    def push(self, val: int) -> None:
        if not self.min_value:
            self.min_value.append(val)
            self.stack.append(val)
        else:
            self.min_value.append(min(val, self.min_value[-1]))
            self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_value.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()