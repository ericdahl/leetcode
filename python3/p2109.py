class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        parts = []
        left = 0
        for sp in spaces:            
            parts.append(s[left:sp])
            parts.append(" ")
            left = sp

        parts.append(s[spaces[-1]:])
        return "".join(parts)
