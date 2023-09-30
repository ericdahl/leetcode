class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        return "".join([c[1] for c in sorted(zip(indices, s))])