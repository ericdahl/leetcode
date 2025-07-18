class Solution:
    def countSegments(self, s: str) -> int:
        # no args means it'll split on any whitespace repeated (different algorithm than if sep is given)
        return len(s.split())
