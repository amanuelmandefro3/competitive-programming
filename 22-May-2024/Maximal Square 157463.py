# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:        
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        _mx = 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1 
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    _mx = max(_mx, dp[i][j])
        
        return _mx * _mx
