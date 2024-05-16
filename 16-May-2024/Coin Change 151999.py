# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in memo:
                return memo[amount]
            min_coins = float('inf')
            for coin in coins:
                if coin <= amount:
                    min_coins = min(min_coins, 1 + dp(amount - coin))
            memo[amount] = min_coins
            return min_coins 
        ans = dp(amount) 
        # return ans if ans else -1  
        return -1 if ans == float('inf') else ans                     
