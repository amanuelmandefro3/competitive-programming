# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, b):
            if i >= len(prices):
                return 0
            if (i,b) in memo:
                return memo[(i,b)]   
            if prices[i] > b:
                memo[(i,b)] = max(prices[i]-b+dp(i+2, float('inf')), dp(i+1,b))
            else:
                memo[(i,b)] = dp(i+1, prices[i])  

            return memo[(i,b)]
        return dp(0, float('inf'))        


        