from sortedcontainers import SortedDict

class SnapshotArray:

    def __init__(self, length: int):
        self.a = []
        self.snap_id = 0
        for i in range(length):
            # use library SortedDict to try to make get() faster
            # though it doesn't seem to help much
            self.a.append(SortedDict({self.snap_id: 0}))

    def set(self, index: int, val: int) -> None:
        self.a[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        l = self.a[index]
        if snap_id in l:
            return l[snap_id]
        snap_id = l.keys()[l.bisect_left(snap_id) - 1]
        return l[snap_id]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)