class MyCalendar:

    def __init__(self):
        self.bookings = SortedList()


    def book(self, startTime: int, endTime: int) -> bool:
        for (b_start, b_end) in self.bookings:
            if startTime < b_end and b_start < endTime:
                return False

        self.bookings.add((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)