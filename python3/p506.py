class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_index = []
        for (i, s) in enumerate(score):
            score_index.append((s, i))

        score_index.sort(reverse=True)

        result = [None] * len(score)

        for rank, (s, i) in enumerate(score_index):
            if rank == 0:
                result[i] = "Gold Medal"
            elif rank == 1:
                result[i] = "Silver Medal"
            elif rank == 2:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank + 1)

        return result
