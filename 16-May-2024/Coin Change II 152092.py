# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(i,amount):
            if amount == 0:
                return 1

            if amount < 0 or i == len(coins):
                return 0 

            if (i,amount) not in memo:
                memo[(i,amount)] = dp(i, amount-coins[i]) + dp(i+1, amount)      

            return memo[(i,amount)]  

        return dp(0,amount)          

        