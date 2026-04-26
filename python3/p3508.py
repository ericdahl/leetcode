class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque([], memoryLimit)
        self.s = set()
        self.dest_packet_timestamps = defaultdict(list)
        self.dest_packet_left = defaultdict(int) # first still valid index

        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        if packet in self.s:
            return False

        if len(self.q) == self.q.maxlen:
            (rm_src, rm_dest, rm_ts) = self.q.popleft()
            self.s.remove((rm_src, rm_dest, rm_ts))
            self.dest_packet_left[rm_dest] += 1
        
        self.q.append(packet)
        self.s.add(packet)
        self.dest_packet_timestamps[destination].append(timestamp)

        return True
        

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []

        packet = self.q.popleft()
        self.s.remove(packet)
        self.dest_packet_left[packet[1]] += 1
        return list(packet)
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:

        arr = self.dest_packet_timestamps[destination]
        left = self.dest_packet_left[destination]

        low = bisect_left(arr, startTime, left)
        high = bisect_right(arr, endTime, left)

        return high - low

        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
