# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            if i not in memo:
                memo[i] = dp(i-1) + dp(i-2)+dp(i-3)
            return memo[i]
        return dp(n)        