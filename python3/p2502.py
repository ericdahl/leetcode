class Allocator:

    def __init__(self, n: int):
        self.mem = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        # note: mID is more like a label of the owner, not a pointer (e.g., malloc). mID can refer to multiple allocated blocks
        contiguous = 0
        for i in range(len(self.mem)):
            if self.mem[i] != 0:
                contiguous = 0
                continue

            if self.mem[i] == 0:
                contiguous += 1
                if contiguous == size:
                    start = i - contiguous + 1
                    for j in range(start, i + 1):
                        self.mem[j] = mID
                    return start
            else:
                contiguous = 0

        return -1
            
        

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for i in range(len(self.mem)):
            if self.mem[i] == mID:
                self.mem[i] = 0
                freed += 1

        return freed
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
