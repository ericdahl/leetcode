class UndergroundSystem:

    def __init__(self):
        self.in_progress = {}
        self.completed = defaultdict(lambda: defaultdict(list))


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_progress[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (start_station, start_time) = self.in_progress.pop(id)
        self.completed[start_station][stationName].append(t - start_time)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return statistics.mean(self.completed[startStation][endStation])



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)