class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0

        n2 = [ord(c) - ord("0") for c in num2]
        n1 = [ord(c) - ord("0") for c in num1]

        for n2_i, n2_d in enumerate(reversed(n2)):
            for n1_i, n1_d in enumerate(reversed(n1)):
                result += n2_d * n1_d * 10 ** n1_i * 10 ** n2_i
        
        return str(result)
