class Solution:
    def greatestLetter(self, s: str) -> str:
        upper = set((c.upper() for c in s if c.isupper()))
        lower = set((c.upper() for c in s if c.islower()))

        both = list(upper & lower)
        both.sort(reverse=True)
        if both:
            return both[0]
        return ""
