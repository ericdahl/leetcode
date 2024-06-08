class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:

        n = len(grid)
        
        for r in range(n):
            for c in range(n):
                if r == c or r + c + 1 == n:
                    if grid[r][c] == 0:
                        return False
                else:
                    if grid[r][c] != 0:
                        return False
        return True
