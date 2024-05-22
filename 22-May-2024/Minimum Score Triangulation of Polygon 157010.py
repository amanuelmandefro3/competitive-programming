# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}
        
        def dp(i, j):
            if j - i < 2:
                return 0
            if (i, j) not in memo:
                ans = float('inf')
                for k in range(i + 1, j):
                    ans = min(ans, dp(i, k) + dp(k, j) + values[i] * values[j] * values[k])
                memo[(i, j)] = ans
            return memo[(i, j)]

        return dp(0, len(values) - 1)