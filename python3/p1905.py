from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid2[0])

        def sink_island(grid: List[List[int]], r: int, c: int) -> List[tuple]:
            stack = [(r, c)]
            cells = []
            while stack:
                x, y = stack.pop()
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                    grid[x][y] = 0  # Mark the cell as visited by sinking the island
                    cells.append((x, y))
                    # Explore all four possible directions
                    stack.extend([(x + dx, y + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]])
            return cells

        def is_sub_island(island: List[tuple]) -> bool:
            return all(grid1[r][c] == 1 for r, c in island)

        sub_island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:  # Found an unvisited part of an island in grid2
                    island_cells = sink_island(grid2, r, c)  # Find all cells in this island
                    if is_sub_island(island_cells):  # Check if this is a sub-island
                        sub_island_count += 1

        return sub_island_count
