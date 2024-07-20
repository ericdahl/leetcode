class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        for i in range(1, 2**16 + 2**15):

            if i > memory1 and i > memory2:
                return [i, memory1, memory2]

            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i

        raise RuntimeError("shouldn't get here")