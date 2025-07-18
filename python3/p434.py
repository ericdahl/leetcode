class Solution:
    def countSegments(self, s: str) -> int:

        count = 0
        last_space = True
        for c in s:
            if c == " ":
                last_space = True
            else:
                if last_space:
                    count += 1
                last_space = False

        return count