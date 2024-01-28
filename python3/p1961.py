class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:

        s_index = 0
        for w in words:
            if s_index >= len(s):
                return True

            if s[s_index:].startswith(w):
                s_index += len(w)
            else:
                return False

        return s_index >= len(s)


