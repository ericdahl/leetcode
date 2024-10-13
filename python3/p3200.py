class Solution:

    @staticmethod
    def max_height(red: int, blue: int, blue_turn: bool) -> int:
        for row in range(1, 200):
            if blue_turn:
                if blue >= row:
                    blue -= row
                    blue_turn = False
                else:
                    return row - 1
            else:
                if red >= row:
                    red -= row
                    blue_turn = True
                else:
                    return row - 1

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(Solution.max_height(red, blue, True), Solution.max_height(red, blue, False))
