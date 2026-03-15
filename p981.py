class TimeMap:

    def __init__(self):
        self.d = defaultdict(SortedDict)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        rtn_val = ""
        sd = self.d[key]
        i = sd.bisect_right(timestamp)
        if i > 0:
            rtn_val = sd.items()[i - 1][1]

        return rtn_val

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)