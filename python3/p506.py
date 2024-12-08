class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_index = []
        for (i, s) in enumerate(score):
            score_index.append((s, i))

        score_index.sort(reverse=True)

        result = [None] * len(score)

        for sii in range(len(score_index)):
            (s, i) = score_index[sii]
            if sii == 0:
                result[i] = "Gold Medal"
            elif sii == 1:
                result[i] = "Silver Medal"
            elif sii == 2:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(sii + 1)

        return result
