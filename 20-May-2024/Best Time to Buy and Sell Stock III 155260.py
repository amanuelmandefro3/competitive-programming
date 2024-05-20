# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, k, have):
            if i == len(prices) or k == 0:
                return 0
            if (i,k, have) in memo:
                return memo[(i,k,have)]    
            if have:
                sell = dp(i+1,k-1, 0) + prices[i]
                do_not_sell = dp(i+1,k, have)
                memo[(i,k,have)] = max(sell, do_not_sell)
            else:
                buy = dp(i+1, k, 1) - prices[i]
                do_not_buy = dp(i+1,k, have)
                memo[(i,k,have)] = max(buy, do_not_buy)    

            return memo[(i,k,have)]

        return dp(0,2,0)    



        