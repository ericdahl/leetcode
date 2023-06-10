class Solution:

    @staticmethod
    def eval_string(s: str) -> str:

        s_stack = []

        for c in s:
            if c == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(c)

        return ''.join(s_stack)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return Solution.eval_string(s) == Solution.eval_string(t)

