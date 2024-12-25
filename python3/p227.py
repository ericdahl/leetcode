class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        num = 0
        op = '+' # default to addition

        for i, ch in enumerate(s):
            # build current number
            if ch.isdigit():
                num = num * 10 + int(ch)

            if ch in "+-*/" or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] = stack[-1] * num
                elif op == '/':
                    stack[-1] = int(stack[-1] / num)

                op = ch
                num = 0

        return sum(stack)
