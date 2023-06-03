class Solution:

    """
    convert pattern into token array
    "ab*c" -> ["a", "b*", "c"]
    """
    @staticmethod
    def tokenize(p: str) -> List[str]:
        tokens = []
        while p:
            if len(p) > 1 and p[1] == "*":
                tokens.append(p[0:2])
                p = p[2:]
            else:
                tokens.append(p[0])
                p = p[1:]

        return tokens


    """
    consolidate/squash any repeats like "a*a*" to "a*"
    """
    @staticmethod
    def consolidate_pattern(tokens: List[str]) -> List[str]:
        for i in range(len(tokens) - 1):
            if len(tokens[i]) > 1 and tokens[i] == tokens[i + 1]:
                tokens[i] = ""

        return [ t for t in tokens if t ]

    @staticmethod
    def is_match(s: List[str], p: List[str]) -> bool:

        if not p:
            if not s:
                # no more characters, "" matches ""
                return True
            return False

        # p[0] is "." or normal char
        if len(p[0]) == 1:
            if not s:
                return False

            if p[0][0] != s[0] and p[0][0] != '.':
                return False

            # normal character matches s[0]
            return Solution.is_match(s[1:], p[1:])

        # p[0] has *

        # check zero matches
        if Solution.is_match(s, p[1:]):
            return True

        for i in range(0, len(s)):
            if s[i] == p[0][0] or p[0][0] == '.':
                if Solution.is_match(s, [p[0][0]] + [p[0][0]] * i + p[1:]):
                    return True


    def isMatch(self, s: str, p: str) -> bool:

        p = Solution.tokenize(p)
        p = Solution.consolidate_pattern(p)

        return Solution.is_match(list(s), p)