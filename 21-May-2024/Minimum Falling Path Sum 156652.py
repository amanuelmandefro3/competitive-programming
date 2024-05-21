# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0]*len(matrix) for _ in range(len(matrix))]

        for c in range(len(matrix[0])):
            dp[0][c] = matrix[0][c]

        def prev_dp(r,c):
            if 0<=r<len(dp) and 0<= c < len(dp[0]):
                return dp[r][c]
            return float('inf')
        for r in range(1,len(matrix)):
            for c in range(len(matrix)):
                dp[r][c] = matrix[r][c] + min(prev_dp(r-1,c-1), prev_dp(r-1,c), prev_dp(r-1,c+1)) 
      

        return min(dp[len(matrix)-1])              
        