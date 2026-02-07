class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        while s:
            result += s[0:k][::-1] + s[k:2*k]
            s = s[2*k:]
        return result
        
