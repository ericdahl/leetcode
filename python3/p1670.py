class FrontMiddleBackQueue:

    def __init__(self):
        self.front = deque()
        self.back = deque()

    def _rebalance(self) -> None:
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        elif len(self.back) > len(self.front):
            self.front.append(self.back.popleft())

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self._rebalance()


    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)


    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._rebalance()

    def popFront(self) -> int:
        if not self.front:
            if not self.back:
                return -1
            return self.back.popleft()
        rtn = self.front.popleft()
        self._rebalance()
        return rtn


    def popMiddle(self) -> int:
        if not self.front:
            if not self.back:
                return -1
            return self.back.pop()

        rtn = self.front.pop()

        self._rebalance()
        return rtn


    def popBack(self) -> int:
        if not self.back:
            if not self.front:
                return -1
            return self.front.pop()

        rtn = self.back.pop()
        self._rebalance()
        return rtn



# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()