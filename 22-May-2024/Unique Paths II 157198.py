# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n,m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        if not obstacleGrid[0][0]: 
            dp[1][1] = 1 

        for i in range(1,n+1):    
            for j in range(1,m+1):
                if not(i==1 and j==1) and obstacleGrid[i-1][j-1] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp,n,m)                    
        return dp[n][m]   

        