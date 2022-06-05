class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for c in s:

            if c in ['(', '{', '[']:
                stack.append(c)
                continue

            if c in [')', ']', '}'] and len(stack) == 0:
                return False

            if c == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False

            if c == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False

            if c == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        return len(stack) == 0