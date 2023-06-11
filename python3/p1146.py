class SnapshotArray:

    def __init__(self, length: int):
        self.a = []
        self.snap_id = 0
        for i in range(length):
            self.a.append({self.snap_id: 0})

    def set(self, index: int, val: int) -> None:
        self.a[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        l = self.a[index]
        snap_id = min(snap_id, max(l.keys()))
        while True:
            if snap_id in l:
                return l[snap_id]
            snap_id -= 1


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)