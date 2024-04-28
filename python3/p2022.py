class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if m * n != len(original):
            return []

        result = []
        while original:
            result.append(original[0:n])
            original = original[n:]
        return result
