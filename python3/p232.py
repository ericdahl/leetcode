class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        

    def push(self, x: int) -> None:
        self.in_stack.append(x)


    def pop(self) -> int:
        if self.out_stack:
            return self.out_stack.pop()

        while len(self.in_stack) > 0:
            popped = self.in_stack.pop()
            self.out_stack.append(popped)
        
        if self.out_stack:
            return self.out_stack.pop()
        
        return self.in_stack.pop()


    def peek(self) -> int:
        if self.out_stack:
            return self.out_stack[-1]

        while len(self.in_stack) > 0:
            popped = self.in_stack.pop()
            self.out_stack.append(popped)

        if self.out_stack:
            return self.out_stack[-1]
        
        return self.in_stack[-1]


    def empty(self) -> bool:
        return not (self.in_stack or self.out_stack)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
