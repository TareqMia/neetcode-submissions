class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        for i in range(len(prices)):
            for j in range(len(prices)):
                x = j + i
        if not prices:
            return 0

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
        