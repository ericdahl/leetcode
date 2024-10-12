class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        count = 0
        d = defaultdict(int)
        for i in range(len(s)):
            d.clear() # re-use to avoid allocating again

            for j in range(i, len(s)):
                d[s[j]] += 1

                if d["0"] <= k or d["1"] <= k:
                    count += 1
                else:
                    break

        return count