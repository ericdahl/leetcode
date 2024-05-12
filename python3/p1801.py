class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        
        buy = [] # heapq (min heap) but values multiplied by -1 to work as max heap
        sell = []

        for order in orders:
            order_price = order[0]
            order_volume = order[1]
            order_buy = (order[2] == 0)
            
            if order_buy:
                while order_volume:
                    
                    if sell and order_price >= sell[0][0]:
                        trans = min(sell[0][1], order_volume)
                        sell[0][1] -= trans
                        order_volume -= trans

                        if sell[0][1] == 0:
                            heapq.heappop(sell)
                    else:
                        heapq.heappush(buy, [-1 * order_price, order_volume])
                        break
            else: # sell order

                while order_volume:
                    
                    if buy and -1 * buy[0][0] >= order_price:
                        trans = min(buy[0][1], order_volume)
                        buy[0][1] -= trans
                        order_volume -= trans

                        if buy[0][1] == 0:
                            heapq.heappop(buy)
                    else:
                        heapq.heappush(sell, [order_price, order_volume])
                        break
        return (sum(s[1] for s in sell) + sum(b[1] for b in buy)) % (10**9 + 7)
