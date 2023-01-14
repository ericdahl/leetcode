class Solution:
    def intToRoman(self, num: int) -> str:
        m = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

        result = []
        m_keys = sorted(m.keys(), reverse=True)

        while num > 0:
            for k in m_keys:
                if k <= num:
                    result += m[k]
                    num -= k
                    break

        return "".join(result)