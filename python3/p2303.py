class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        # adjust bracket thresholds so each is the next incremental tax
        for i in range(len(brackets) - 1, 0, -1):
            brackets[i][0] -= brackets[i - 1][0]

        tax = 0
        income_taxed = 0

        while income_taxed < income:
            bracket = brackets.pop(0)
            bracket_threshold = bracket[0]
            bracket_rate = bracket[1] / 100

            bracket_income = min(income - income_taxed, bracket_threshold)
            tax += bracket_income * bracket_rate
            income_taxed += bracket_income

        return tax
