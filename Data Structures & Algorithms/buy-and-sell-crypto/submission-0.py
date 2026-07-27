class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0
        for i, p in enumerate(prices):
            if i == 0:
                continue
            profit = p - minBuy
            if p < minBuy:
                minBuy = p
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit
            