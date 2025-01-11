class Solution:
    def checkRecord(self, s: str) -> bool:

        a_days = 0
        l_cons = 0

        for c in s:
            if c == "A":
                a_days += 1
                if a_days >= 2:
                    return False

            if c == "L":
                l_cons += 1
                if l_cons >= 3:
                    return False
            else:
                l_cons = 0
        return True
