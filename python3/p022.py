class Solution:

    @staticmethod
    def is_valid(s):
        opens = 0
        for c in s:
            if c == '(':
                opens += 1
            else:
                opens -= 1
                if opens < 0:
                    return False
        return opens == 0

    def generateParenthesis(self, n: int) -> List[str]:

        # very inefficient, but still fast enough for n <= 8
        results = []
        for i in product('()', repeat = 2 * n):
            if Solution.is_valid(i):
                results.append(''.join(i))

        return results
