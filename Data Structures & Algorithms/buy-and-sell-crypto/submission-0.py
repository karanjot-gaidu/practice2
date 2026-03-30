class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            max_price = 0
            for j in range(i+1, len(prices)):
                max_price = max(prices[j], max_price)
            max_profit = max(max_profit, max_price - prices[i])
        return max_profit