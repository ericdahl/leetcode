class Solution:
    def winningPlayer(self, x: int, y: int) -> str:

        alice_turn = True

        # valid move: 75 + 4 * 10
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            alice_turn = not alice_turn

        if alice_turn:
            return "Bob"
        return "Alice"
