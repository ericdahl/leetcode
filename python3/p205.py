class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}

        for i,c in enumerate(s):

            if c not in mapping:

                # if letter is already mapped, not valid
                if t[i] in mapping.values():
                    return False

                mapping[c] = t[i]
            else:
                if t[i] != mapping[c]:
                    return False
        return True
