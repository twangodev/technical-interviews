class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(1, len(prices)):
            difference = prices[i] - prices[i - 1]
            profit += max(difference, 0)

        return profit