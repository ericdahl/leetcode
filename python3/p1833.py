class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        bars = 0
        costs.sort()
        while costs and coins >= costs[0]:
            bars += 1
            coins -= costs.pop(0)

        return bars
