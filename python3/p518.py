class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted([c for c in coins if c <= amount], reverse=True)

        # dynamic programming - # of ways to make amount i
        ways = [0] * (amount + 1)
        ways[0] = 1 # base case - 1 way to make 0 coins

        for c in coins:
            for i in range(c, amount + 1):
                ways[i] += ways[i - c]

        return ways[amount]
