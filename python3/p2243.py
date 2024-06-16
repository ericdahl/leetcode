class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            new = []
            for i in range(0, len(s), k):
                
                # alternative: 
                # while s:
                #   g, s = s[0:k], s[k:]
                # looks nicer to me but slower as it modifies s more
                new += str(sum(int(c) for c in s[i:i+k]))
            s = "".join(new)

        return s
