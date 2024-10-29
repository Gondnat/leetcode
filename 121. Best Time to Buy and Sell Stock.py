class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        j = 0
        while j < len(prices):
            if prices[j] > prices[i]:
                max_profit = max(max_profit, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return max_profit