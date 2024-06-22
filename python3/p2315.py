class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum([sub.count("*") for sub in islice(s.split("|"), None, None, 2)])

        
