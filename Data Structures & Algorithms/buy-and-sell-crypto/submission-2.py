class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        best = 0

        for sell in prices[1:]:
            profit = sell - buy
            best = max(best, profit)

            if sell < buy:
                buy = sell

        return best