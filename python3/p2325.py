class Solution:
    def decodeMessage(self, key: str, message: str) -> str:

        m = {" " : " "}
        curr = 'a'
        for c in key:
            if c not in m and c != " ":
                m[c] = curr
                curr = chr(ord(curr) + 1)

        return "".join([m[c] for c in message])