class Solution:

    """
    consolidate/squash any repeats like "a*a*" to "a*"
    # """
    @staticmethod
    def consolidate_pattern(p: str) -> str:
        tokens = list(p)
        for i in range(len(tokens) - 1):
            if tokens[i] == "*" and tokens[i + 1] == "*":
                tokens[i] = ""

        return "".join([ t for t in tokens if t ])


    @staticmethod
    def is_match(s: str, p: str, checks) -> bool:

        if not p:
            if not s:
                # no more characters, "" matches ""
                return True
            return False

        # already checked this, skip all remaining checks
        if (s, p) in checks:
            return False

        checks.add((s, p))

        # p[0] is "." or normal char
        if p[0] != "*":
            if not s or (p[0] != s[0] and p[0] != '?'):
                return False

            return Solution.is_match(s[1:], p[1:], checks)

        # p[0] has *

        # check zero matches
        if Solution.is_match(s, p[1:], checks):
            return True

        for i in range(1, len(s) + 1):
            if Solution.is_match(s[i:], p, checks):
                return True


    def isMatch(self, s: str, p: str) -> bool:

        # short circuit logic - if pattern has more non-* chars than s, no match
        pp = [c for c in p if c != '*']
        if len(pp) > len(s):
            return False

        p = Solution.consolidate_pattern(p)

        return Solution.is_match(s, p, set())