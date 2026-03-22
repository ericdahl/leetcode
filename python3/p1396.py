class UndergroundSystem:

    def __init__(self):
        # in progress train rides.
        #   user_id -> (start_station, start_time)
        self.in_progress = {}

        # completed train ride times
        #  (start_station, end_station) -> (total_ride_duration, total_ride_count)
        self.completed = defaultdict(lambda: (0, 0))


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_progress[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (start_station, start_time) = self.in_progress.pop(id)

        key = (start_station, stationName)
        old_total, old_count = self.completed[key]

        new_total = old_total + (t - start_time)
        new_count = old_count + 1
        self.completed[key] = (new_total, new_count)



    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.completed[(startStation, endStation)]
        return total / count



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)