class MedianFinder:

    def __init__(self):
        self.ol = SortedList()


    def addNum(self, num: int) -> None:
        self.ol.add(num)


    def findMedian(self) -> float:
        l = len(self.ol)
        if l % 2 == 0:
            return 0.5 * (self.ol[l // 2] + self.ol[l // 2 - 1])
        return self.ol[l//2]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()