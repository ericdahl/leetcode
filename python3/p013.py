class Solution:
    def romanToInt(self, s: str) -> int:

        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        digits = [mapping[c] for c in s]

        total = 0
        while digits:
            if len(digits) >= 2 and digits[0] < digits[1]:
                total += digits[1] - digits[0]
                digits = digits[2:]
            else:
                total += digits.pop(0)

        return total
