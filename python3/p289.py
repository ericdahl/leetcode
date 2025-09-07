class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:


        def neighbors(r: int, c: int) -> int:
            n = 0
            for cn in [c-1, c, c +1 ]:
                for rn in [r - 1, r, r + 1]:
                    if cn == c and rn == r:
                        continue
                    if rn < 0 or cn < 0:
                        continue
                    if rn >= len(board) or cn >= len(board[0]):
                        continue

                    n += board[rn][cn]

            return n

        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        # need to track updates to do all-at-once
        to_kill, to_birth = [], []

        for r in range(rows):
            for c in range(cols):
                n = neighbors(r, c)
                if board[r][c] == 1 and n < 2 or n > 3:
                    to_kill.append((r, c))
                if board[r][c] == 0 and n == 3:
                    to_birth.append((r, c))

        for (tk_r, tk_c) in to_kill:
            board[tk_r][tk_c] = 0

        for (tb_r, tb_c) in to_birth:
            board[tb_r][tb_c] = 1
