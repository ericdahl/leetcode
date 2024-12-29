class Solution:


    @staticmethod
    def find_islands(grid: List[List[int]]) -> List[set[int]]:
        rows = len(grid)
        cols = len(grid[0])
        islands = {}

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue

                if not (r, c-1) in islands and not (r-1, c) in islands:
                    # new island
                    islands[(r,c)] = set([(r,c)])

                if (r, c - 1) in islands and (r - 1, c) in islands:
                    # merge two islands from left and above
                    left = islands[(r, c - 1)]
                    above = islands[(r - 1, c)]
                    merged = left | above | {(r, c)}
                    for key in list(islands.keys()):
                        if islands[key] == left or islands[key] == above:
                            islands[key] = merged

                    islands[(r,c)] = merged

                elif c > 0 and (r, c - 1) in islands:
                    # existing island to left
                    islands[(r, c)] = islands[(r, c - 1)]
                    islands[(r, c)].add((r, c))
                elif r > 0 and (r - 1, c) in islands:
                    # existing island above
                    islands[(r, c)] = islands[(r - 1, c)]
                    islands[(r, c)].add((r, c))



        unique_islands = {frozenset(isl) for isl in islands.values()}
        return [set(isl) for isl in unique_islands]

        # print(f"s_islands: s_islands)
        # print(len(s_islands))
        # return s_islands.values()

        # print(len(set(islands.values())))

    @staticmethod
    def is_subisland(sub:set, main: set):
        return sub.issubset(main)



    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        g1_islands = Solution.find_islands(grid1)
        g2_islands = Solution.find_islands(grid2)

        subs = 0
        for g2i in g2_islands:
            for g1i in g1_islands:
                if Solution.is_subisland(g2i, g1i):
                    subs += 1
                    break

        return subs



