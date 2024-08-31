class Solution:
    def minimumChairs(self, s: str) -> int:

        people = 0
        min_chairs = 0

        for c in s:
            if c == "E":
                people += 1
            else:
                people -= 1
            min_chairs = max(min_chairs, people)
        return min_chairs