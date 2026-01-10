class MyCalendar:

    def __init__(self):
        self.bookings = SortedList()


    def book(self, startTime: int, endTime: int) -> bool:
        idx = self.bookings.bisect_left((startTime, endTime))

        if idx > 0:
            prev_start, prev_end = self.bookings[idx - 1]
            if prev_end > startTime:
                return False

        if idx < len(self.bookings):
            next_start, next_end = self.bookings[idx]
            if next_start < endTime:
                return False

        self.bookings.add((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)