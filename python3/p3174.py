class Solution:
    def clearDigits(self, s: str) -> str:
        a = list(s)

        digits = ((c_i, c) for (c_i, c) in enumerate(s) if str.isdigit(c))
        for d_i, d in digits:

            a[d_i] = ''

            for j in range(d_i, -1, -1):
                if str.isalpha(a[j]):
                    a[j] = ''
                    break

        return ''.join(a)