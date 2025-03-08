class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v = set("aeiou")
        start_end = [int(w[0] in v and w[-1] in v) for w in words]

        s = 0
        prefix_sum = []
        for se in start_end:
            s += se
            prefix_sum.append(s)

        # to handle special case where l=0
        prefix_sum.append(0)

        return [prefix_sum[r] - prefix_sum[l - 1] for (l,r) in queries]