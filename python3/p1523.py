class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            odds += 1
        return odds
