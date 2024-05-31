import sortedcontainers

class MKAverage:

    def __init__(self, m: int, k: int):
        self.l = sortedcontainers.SortedList([])
        self.dq = deque([], m + 1) # track last m+1 items to discard oldest item from l
        self.m = m
        self.k = k

    def addElement(self, num: int) -> None:
        self.l.add(num)
        self.dq.append(num)
        if len(self.l) > self.m:
            self.l.discard(self.dq[0])


    def calculateMKAverage(self) -> int:
        if len(self.l) < self.m:
            return -1
        
        buffer = self.l[self.k:-self.k]
        return sum(buffer) // len(buffer)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
