class Solution:
    def largestOddNumber(self, num: str) -> str:
        for last_idx in range(len(num) - 1, -1, -1):
            if int(num[last_idx]) % 2 == 1:
                return num[0:last_idx + 1]
        return ""
