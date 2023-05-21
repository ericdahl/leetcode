class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"

        s = Solution.countAndSay(self, n - 1)

        new_s = ""
        last_c = s[0]
        last_count = 0
        for c in s + "X":
            if c == last_c:
                last_count += 1
            else:
                new_s += str(last_count) + last_c
                
                last_c = c
                last_count = 1

        return new_s

