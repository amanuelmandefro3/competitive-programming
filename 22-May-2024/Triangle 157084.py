# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0]*len(triangle[i]) for i in range(len(triangle))]
        def bound(r,c):
            if 0 <= r < len(triangle) and 0<= c < len(triangle[r]):
                return dp[r][c]
            return float('inf')    
        dp[0][0] = triangle[0][0]
        for r in range(1,len(triangle)):
            for c in range(len(triangle[r])):
                dp[r][c] = triangle[r][c] + min(bound(r-1,c), bound(r-1,c-1))
        print(dp)
        return min(dp[-1])               

        