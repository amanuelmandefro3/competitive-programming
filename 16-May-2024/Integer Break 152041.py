# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            ans = 0
            for j in range(1,n):
                ans = max(ans, j*dp(i-j))
            memo[i] = ans
            return memo[i]
        return dp(n)        

        