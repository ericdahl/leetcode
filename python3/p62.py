class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # without cache, this is too slow - short-circuit repeated calls
        @cache
        def dp(r, c):
            if r == 1 or c == 1:
                return 1
            return dp(r - 1, c) + dp(r, c - 1)
        
        return dp(m, n)
