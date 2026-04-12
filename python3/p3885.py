class EventManager:

    def __init__(self, events: list[list[int]]):

        # min heap to store -priority,event history. Don't remove items for speed
        self.hq = []

        # dist of event_id -> priority. Items removed. Source of Truth
        self.priorities = {}

        for (event_id, priority) in events:
            heapq.heappush(self.hq, (-priority, event_id))
            self.priorities[event_id] = priority


    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.priorities[eventId] = newPriority
        heapq.heappush(self.hq, (-newPriority, eventId))
        

    def pollHighest(self) -> int:
        while self.hq:
            priority, event_id = heapq.heappop(self.hq)

            # check if event is still active and the priority of it is still accurate
            if event_id in self.priorities and self.priorities[event_id] == -priority:
                del self.priorities[event_id]
                return event_id
        return -1
        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()
