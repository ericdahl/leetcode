class CustomStack:

    def __init__(self, maxSize: int):
        self.a = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.a) == self.max_size:
            return

        self.a.append(x)


    def pop(self) -> int:
        if not self.a:
            return -1

        return self.a.pop()


    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.a), k)):
            self.a[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)