class Solution:
    def firstUniqChar(self, s: str) -> int:

        d = defaultdict(list)
        for c_index, c in enumerate(s):
            d[c].append(c_index)

        uniques = []
        for k, v in d.items():
            if len(v) == 1:
                uniques.append(v[0])

        return min(sorted(uniques), default = -1)
