class Solution:
    def getLucky(self, s: str, k: int) -> int:

        result = "".join([str(ord(c) - ord("a") + 1) for c in s])

        for i in range(k):
            result = str(sum([int(c) for c in result]))

        return int(result)
        
