class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        freq = defaultdict(int)

        for n in arr:
            freq[((n % k) + k) % k] += 1

        for i in range(1, k // 2 + 1):
            if freq[i] != freq[k - i]:
                return False

        # special case when k is even, need to ensure that the middle remainder count is even
        if k % 2 == 0 and freq[k // 2] % 2 != 0:
            return False

        return True