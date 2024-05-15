# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}

        def dp(i, b):
            if i == len(prices):
                return 0
            if (i, b) in memo:
                return memo[(i, b)]
            if prices[i] > b+fee:
                memo[(i, b)] = max(prices[i] - b - fee + dp(i + 1, float('inf')), dp(i + 1, b))
            else:
                b = min(b, prices[i])
                memo[(i, b)] = dp(i + 1, b)
            return memo[(i, b)]

        return dp(0, float('inf'))
